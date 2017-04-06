
# coding: utf-8

# ## Employee Compensation Analysis

# ### Find out the highest paid departments in each organization group by calculating mean of total compensation for every department

# In[16]:

import numpy as np
import pandas as pd
import os
import datetime


# In[17]:

# Read compensation csv into a dataframe
df = pd.read_csv('Data/employee_compensation.csv')


# In[18]:

# Select relevant columns
df = df[['Organization Group', 'Department', 'Total Compensation']]


# In[19]:

# Group the records by departments in each organization and calculate the mean total compensation for each department
groupby_org_dept = df.groupby(by=['Organization Group', 'Department'])
groupby_org_dept = groupby_org_dept.mean()
final_org_dept = groupby_org_dept.reset_index()
final_org_dept.head()


# In[20]:

# Group records by organization showing department with maximun total compensation
final_org_dept = final_org_dept.groupby(by='Organization Group').agg({'Total Compensation':max, 'Department':max})
final_org_dept.head()


# In[21]:

os.makedirs('Output', exist_ok=True)


# In[23]:

final_org_dept.to_csv('Output/Q2Part1.csv')


# In[24]:

print('Completed the analysis for fetching organizations along with their corresponding departments with maximum total compensation . Output is saved as a csv file in the location Output/Q2Part1.csv')


# In[ ]:



