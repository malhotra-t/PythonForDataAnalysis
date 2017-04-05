
# coding: utf-8

# ## NYC Collision Analysis

# In[1]:

import numpy as np
import pandas as pd
import datetime
import os


# In[2]:

# Read csv file into a dataframe
df = pd.read_csv('Data/vehicle_collisions.csv', index_col = 0, parse_dates=[1])


# In[3]:

df.head()


# In[4]:

# Filter to get all 2016 records
df = df[ (df['DATE'] > datetime.date(year=2015,month=12,day=31)) & (df['DATE'] < datetime.date(year=2017,month=1,day=1))]


# In[5]:

# Extract month from the date column
df['MONTH']= df['DATE'].apply(lambda x: x.month)


# In[6]:

# Filter records for Manhattan
df_manhattan = df[df['BOROUGH'] == 'MANHATTAN']


# In[7]:

# Group all the records for each month
df = df.groupby(by='MONTH').count()


# In[8]:

# Renaming the Date column header to indicate the count of collisions in NYC in the new dataframe
df['NYC'] = df['DATE']
df = df['NYC']
df.head()


# In[9]:

# Group the records in Manhattan dataframe for each month
df_manhattan = df_manhattan.groupby(by='MONTH').count()
# Renaming the Date column header to indicate the count of collisions in Manhattan in the new dataframe
df_manhattan['MANHATTAN'] = df_manhattan['DATE']
df_manhattan = df_manhattan['MANHATTAN']


# In[10]:

# Concatenating the dataframes for Manhattan and NYC
final_percentage = pd.concat([df_manhattan,df], axis=1)


# In[11]:

# Calculating the percentage of collisions in Manhattan to NYC and adding the column in the final dataframe
final_percentage['PERCENTAGE'] = final_percentage['MANHATTAN'] / final_percentage['NYC']


# In[12]:

# Creating the output folder
os.makedirs('Output', exist_ok=True)


# In[13]:

# Saving the final csv in the Output folder
final_percentage.to_csv('Output/Q1Part1.csv')


# In[14]:

print('Completed the analysis for calculating percentage of collisions in Manhattan compared to those in NYC for each month. Output is saved as a csv file in the location Output/Q1Part1.csv')


# In[ ]:



