--POCUS
-- for taking out pregnancy ids of famli participants
WITH preg_ids1 AS (
SELECT * FROM (
 SELECT 
        f.famli_id, 
        f.vr_id, 
        CAST(f."date" AS DATE) AS f_date, 
        CAST(cavs."eventdate" AS DATE) AS cavs_eventdate, 
        CAST(cavs."version" AS DATE) AS cavs_version,  
        cavs.current_pregnancy_id, 
        DENSE_RANK() OVER (
            PARTITION BY cavs.current_pregnancy_id 
            ORDER BY DATEDIFF(day,  CAST (cavs."eventdate" AS DATE) , CAST (f."date" AS DATE))
			
		                
        ) AS rn
FROM kobo.famlipocus49 f 
LEFT JOIN opensrpdb.client ctt ON ctt.identifiers_opensrp_id = f.vr_id 
LEFT JOIN opensrpdb."Conduct_ANC_Visit_staging" cavs ON cavs.baseentityid = ctt."baseEntityId" 
)  a
WHERE rn = 1 --and eventdate::date >= '2024-03-16'
),
-----------------------------------------------------COMP-------------------------------------------
 preg_ids AS (
    SELECT * 
    FROM (
        SELECT *, 
            DENSE_RANK() OVER (
                PARTITION BY famli_id 
                ORDER BY CAST ( cavs_version AS date) DESC
            ) AS rn3 
        FROM preg_ids1
    ) a 
    WHERE rn3 = 1
)
--SELECT * FROM  preg_ids
-----xxx-------------
-- simply pulling out values from the pocus table as needed according to CRF, joining the above CTE to fetch pregnancy IDs

SELECT DISTINCT 
    f.famli_id AS pid, 
    p.current_pregnancy_id AS id_chk,
    FORMAT(CAST(f."date" AS DATE), 'dd/MM/yyyy') AS date, 
    f."visit_number" AS visn,
    CASE 
        WHEN f.baby IS NULL THEN 'A' 
        ELSE f.baby 
    END AS baby,
    'handheld' AS handheld, 
    CASE
        WHEN f."blind_sweeps" = 'performed' THEN '1'
        WHEN f."blind_sweeps" = 'not_performed' THEN '0'
        ELSE '98'
    END AS blindswp,
    CASE
        WHEN f."fetal_movement" = 'present' THEN '1'
        WHEN f."fetal_movement" = 'absent' THEN '2'
        WHEN f."fetal_movement" = 'not_performed' THEN '0'
    END AS fetmov,
    CASE
        WHEN f."cardiac_activity_sweeps" = 'performed' THEN '1'
        WHEN f."cardiac_activity_sweeps" = 'not_performed' THEN '0'
    END AS cadac, 
    f."fetal_heart_rate_today" AS fhr,
    CASE 
        WHEN f."fetal_heart_rate_today_001_regular" = 1 THEN '1'
        WHEN f."fetal_heart_rate_today_001_regular" = 0 THEN '2'
        ELSE '0'
    END AS fhr_st,
    CASE 
        WHEN f."four_chambered_view_of_heart" = 'well_seen' THEN '1'
        WHEN f."four_chambered_view_of_heart" = 'not_well_seen' THEN '2'
        WHEN f."four_chambered_view_of_heart" = 'not_performed' THEN '0'
    END AS cham,
    CASE
        WHEN f."biometry_sweeps" = 'performed' THEN '1'
        WHEN f."biometry_sweeps" = 'not_performed' THEN '0'
    END AS bioswp,
    CASE
        WHEN f."umbilical_artery_doppler_sweeps" = 'performed' THEN '1'
        WHEN f."umbilical_artery_doppler_sweeps" = 'not_performed' THEN '0'
    END AS uad,
    CASE
        WHEN f."was_the_procedure_prematurely_stopped" = 'no' THEN '0'
        WHEN f."was_the_procedure_prematurely_stopped" = 'yes' THEN '1'
    END AS pro, 
    CASE
        WHEN f."please_specify_the_primary_reason" = 'na__not_stopped_prematurely' THEN '98'
        WHEN f."please_specify_the_primary_reason" = 'device_failure' THEN '1'
        WHEN f."please_specify_the_primary_reason" = 'malfunction' THEN '2'
        WHEN f."please_specify_the_primary_reason" = 'user_error' THEN '3'
        WHEN f."please_specify_the_primary_reason" LIKE 'other' THEN '4'
    END AS fail_re,
    NULL AS othfail_rea, 
    CASE
        WHEN f."were_any_device_deficiencies_r" = 'no' THEN '0'
        WHEN f."were_any_device_deficiencies_r" = 'yes' THEN '1'
    END AS def,
    CASE 
        WHEN f."were_any_device_deficiencies_r" = 'yes' THEN f."if_yes_what_type_of_deficienc"  
        ELSE NULL 
    END AS def_sp,
    'expertuseraku' AS comp,
    FORMAT(CAST(f."date" AS DATE), 'DD/MM/YYYY') AS datecomp
FROM kobo.famlipocus49 f

LEFT JOIN preg_ids p ON f.famli_id = p.famli_id
WHERE CAST(f."date" AS DATE) <= '2024-08-14'
