-- Define the CTE to get the vr_id from raw_sheets.daily_log_staging and join with opensrpdb.client
use staging;

WITH CTE_Current AS (
    SELECT 
        dls.vr_id,
        cli.baseentityid,
        dls.date_of_us -- Add date_of_us column here
    FROM 
        raw_sheets.daily_log_staging AS dls
    LEFT JOIN 
        opensrpdb.client AS cli
    ON 
        dls.vr_id = cli.identifiers_opensrp_id
)

-- Main query
SELECT 
    CTE_Current.vr_id, -- Add vr_id from CTE
    CAST(lp.version AS DATE) AS initial_dt,
    (CASE 
        WHEN lpo.version IS NOT NULL THEN CAST(lpo.version AS DATE)
        ELSE CAST(GETDATE() AS DATE)
    END) AS end_dt,
    CTE_Current.date_of_us, -- Include date_of_us from CTE
    DATEDIFF(
        DAY, 
        CAST(lp.version AS DATE), 
        CASE 
            WHEN lpo.version IS NOT NULL THEN CAST(lpo.version AS DATE)
            ELSE GETDATE()
        END
    ) AS DateDifference,
    lpo.pregnancy_id
FROM 
    opensrpdb.log_pregnancy_staging AS lp 
LEFT JOIN 
    opensrpdb.log_pregnancy_outcome_staging AS lpo 
ON 
    lp._id = lpo.pregnancy_id
 JOIN 
    CTE_Current -- Join with the CTE to get vr_id and date_of_us
ON 
    CTE_Current.baseentityid = lp.baseentityid -- Adjust this if needed
	and
	CTE_Current.date_of_us between CAST(lp.version AS DATE) and
    (CASE 
        WHEN lpo.version IS NOT NULL THEN CAST(lpo.version AS DATE)
        ELSE CAST(GETDATE() AS DATE)
    END)
WHERE 
    CAST(lp.version AS DATE) IS NOT NULL 
   --ND lp.locationid = 'ec46913a-a2d6-4f9e-a2f3-4ac36f32ac34'
  /*  AND CTE_Current.date_of_us BETWEEN CAST(lp.version AS DATE) AND 
    CASE 
        WHEN lpo.version IS NOT NULL THEN CAST(lpo.version AS DATE)  
        ELSE GETDATE() 
    END */
    AND lpo.pregnancy_id IS NOT NULL -- Add filter for pregnancy_id
ORDER BY 
    vr_id;


	
/*select baseentityid,permanent_location from opensrpdb.client

group by baseentityid

having permanent_location is null*/ 

