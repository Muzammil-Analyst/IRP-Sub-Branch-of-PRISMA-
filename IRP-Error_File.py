#!/usr/bin/env python
# coding: utf-8

# In[132]:


import numpy as np
import pandas as pd


# In[ ]:


dataANC = pd.read_csv("anc_dataset.csv", encoding='utf-8-sig')


# In[2]:


dataANC.head()


# In[55]:


dataANC.info()


# In[56]:


def duplicate_check(dataANC):
    duplicate=dataANC.duplicated().any()
    return duplicate


# In[7]:


# Get the count of null values for each column
null_counts = dataANC.isnull().sum()

print("Null value counts for each column:")
for column, count in null_counts.items():
    print(f"{column}: {count}")


# In[124]:


def create_error_check(dataANC, condition, field_name, error_value, remarks):
    selected_columns = ['VPTID/VRID','PW_ID','Visit Number']
    error_checks = dataANC.loc[condition , selected_columns]
    error_checks['Field Name'] = field_name  # Combine field names if multiple
    error_checks['Error Value'] = error_value  # Convert to strings and join
    error_checks['Remarks'] = remarks



    pd.set_option('display.max_rows', 1000)
    return error_checks


# In[68]:


dataANC['Averagereadingdiastolic '].dtype


# # WEIGHT RANGE ERROR

# In[40]:


remarks = " Weight should be in between 25 to 135 kg."
dataANC['weight'] = pd.to_numeric(dataANC['weight'], errors='coerce')
condition = (dataANC['weight'] <= 25) | (dataANC['weight'] >=135)
field_name = "weight"
error_value = dataANC["weight"]
result = create_error_check(dataANC, condition, field_name, error_value, remarks)

#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
result
#result.to_excel('error_report_A6.xlsx', index=True)
#No-Error


# # HEIGHT RANGE ERROR

# In[41]:


remarks = " Height should be less then  130cm  or Greater then 190cm"
dataANC['Height(cm)'] = pd.to_numeric(dataANC['Height(cm)'], errors='coerce')
condition = (dataANC['Height(cm)'] < 130) | (dataANC['Height(cm)'] >= 190)
field_name = 'Height(cm)'
error_value = dataANC['Height(cm)'] 
result = create_error_check(dataANC, condition, field_name, error_value, remarks)

#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
result
#result.to_excel('error_report_A6.xlsx', index=True)


# # MUAC RANGE ERROR

# In[42]:


remarks = " MUAC is Less then 11 or MUAC is Greater then 47 "
dataANC['MUACcm'] = pd.to_numeric(dataANC['MUACcm'], errors='coerce')
condition = (dataANC['MUACcm'] <= 11) | (dataANC['MUACcm'] >= 47)
field_name = 'MUACcm'
error_value = dataANC['MUACcm'] 
result = create_error_check(dataANC, condition, field_name, error_value, remarks)

#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
result
#result.to_excel('error_report_A6.xlsx', index=True)


# # TEMPRATURE RANGE ERROR

# In[43]:


remarks = "Temprature is less then 96 Fahrenheit or Temprature is Greater then 108"
dataANC['Temperature'] = pd.to_numeric(dataANC['Temperature'], errors='coerce')
condition = (dataANC['Temperature'] <= 96) | (dataANC['Temperature'] >= 108)
field_name = dataANC['Temperature']
error_value = dataANC['Temperature'] 
result = create_error_check(dataANC, condition, field_name, error_value, remarks)

#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
result
#result.to_excel('error_report_A6.xlsx', index=True)


# # HEART-RATE RANGE ERROR

# In[45]:


remarks = "Heart-Rate is Less then 40 or Heart-Rate is Greater then 170 "
dataANC['Heartrate'] = pd.to_numeric(dataANC['Heartrate'], errors='coerce')
condition = (dataANC['Heartrate'] <= 40) | (dataANC['Heartrate'] >=170)
field_name = 'Heartrate'
error_value = dataANC['Heartrate'] 
result = create_error_check(dataANC, condition, field_name, error_value, remarks)

#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
result
#result.to_excel('error_report_A6.xlsx', index=True)


# # First-Reading-Systollic RANGE ERROR

# In[46]:


remarks = "First-Reading-Systollic BP is Less then 60 or First-Reading-Systollic BP Greater then 200 "
dataANC['FirstReadingsystolicBP'] = pd.to_numeric(dataANC['FirstReadingsystolicBP'], errors='coerce')
condition = (dataANC['FirstReadingsystolicBP'] <= 60) | (dataANC['FirstReadingsystolicBP'] >= 200)
field_name = 'FirstReadingsystolicBP'
error_value = dataANC['FirstReadingsystolicBP'] 
result = create_error_check(dataANC, condition, field_name, error_value, remarks)

#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
result
#result.to_excel('error_report_A6.xlsx', index=True)


# # First-Reading-Diastollic  RANGE ERROR

# In[48]:


remarks = "First-Reading-Diastollic BP is Less then 40 or First-Reading-Diastollic BP Greater then 130 count "
dataANC['FirstreadingdiastolicBP'] = pd.to_numeric(dataANC['FirstreadingdiastolicBP'], errors='coerce')
condition = (dataANC['FirstreadingdiastolicBP'] <= 40) | (dataANC['FirstreadingdiastolicBP'] >= 130)
field_name = 'FirstreadingdiastolicBP'
error_value = dataANC['FirstreadingdiastolicBP'] 
result = create_error_check(dataANC, condition, field_name, error_value, remarks)

#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
result
#result.to_excel('error_report_A6.xlsx', index=True)


#  # Second-Reading-Systollic RANGE ERROR

# In[49]:


remarks = "Second-Reading-Systollic is Less then 60 or Second-Reading-Systollic is Greater Then 200"
dataANC['Secondreadingsystolic '] = pd.to_numeric(dataANC['Secondreadingsystolic '], errors='coerce')
condition = (dataANC['Secondreadingsystolic '] <= 60) | (dataANC['Secondreadingsystolic '] >= 200)
field_name = 'Secondreadingsystolic'
error_value = dataANC['Secondreadingsystolic '] 
result = create_error_check(dataANC, condition, field_name, error_value, remarks)

#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
result
#result.to_excel('error_report_A6.xlsx', index=True)


# # Second-Reading-Diastollic RANGE ERROR

# In[49]:


remarks = "Second-Reading-Diastollic is Less then 40 or Second-Reading-Diastollic is Greater then 130"
dataANC['Secondreadingdiastolic '] = pd.to_numeric(dataANC['Secondreadingdiastolic '], errors='coerce')
condition = (dataANC['Secondreadingdiastolic '] <= 40) | (dataANC['Secondreadingdiastolic '] >= 130)
field_name ='Secondreadingdiastolic '
error_value = dataANC['Secondreadingdiastolic '] 
result = create_error_check(dataANC, condition, field_name, error_value, remarks)

#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
result
#result.to_excel('error_report_A6.xlsx', index=True)


# In[140]:


dataANC["DifferenceBPReading"]=dataANC["Averagereadingsystolic "] - dataANC["Averagereadingdiastolic "]


# In[162]:


remarks = 'Average reading of Systolic and Diastolic are less than 20, Average Systiloc:' +dataANC['Averagereadingsystolic '].astype(str)+ ' and Average Diastolic:' +dataANC['Averagereadingdiastolic '].astype(str)

dataANC['Averagereadingsystolic '] = pd.to_numeric(dataANC['Averagereadingsystolic '], errors='coerce')
dataANC['Averagereadingdiastolic '] = pd.to_numeric(dataANC['Averagereadingdiastolic '], errors='coerce')

condition = (dataANC['Averagereadingsystolic '] > dataANC['Averagereadingdiastolic '] ) & (dataANC["DifferenceBPReading"] < 20)
field_name ='DifferenceBPReading'

#error_value = dataANC['DifferenceBPReading'] +dataANC['Averagereadingsystolic ']
error_value = dataANC['DifferenceBPReading'].astype(str)

result = create_error_check(dataANC, condition, field_name, error_value, remarks)

#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
result
result.to_excel('error_report_A6sas.xlsx', index=True)


# In[53]:


pd.set_option('display.max_rows', 20000)
dataANC.groupby(['VPTID/VRID','Height(cm)'])['PW_ID'].count()


# In[169]:


count_df = dataANC.groupby(['PW_ID', 'Height(cm)']).size().reset_index(name='count').sort_values(by=['PW_ID'])
count_df


# In[163]:


# This code identifies the discrepancy of count in PW_ID according to Height

# Group by PW_ID and Height(cm) and count occurrences
count_df = dataANC.groupby(['PW_ID', 'Height(cm)']).size().reset_index(name='count')

# Identify PW_IDs with discrepant counts
discrepant_pw_ids = count_df.groupby('PW_ID').filter(lambda x: x['count'].nunique() > 1)['PW_ID'].unique()

# Create error check
remarks = "Discrepancy in count for PW_ID and Height(cm)"
dataANC['Height(cm)'] = pd.to_numeric(dataANC['Height(cm)'], errors='coerce')

condition = dataANC['PW_ID'].isin(discrepant_pw_ids)
error_value = dataANC['Height(cm)']
field_name = 'Height(cm)'


result = create_error_check(dataANC, condition, field_name, error_value, remarks)
# Merge count information into the result DataFrame



#field_name_class_str = str(type(field_name))
result.reset_index(drop=True, inplace=True)
result.index += 1
result
#result.to_excel('error_report_A6.xlsx', index=True)


# In[ ]:





# In[ ]:




