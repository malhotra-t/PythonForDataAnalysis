
# coding: utf-8

# ## EMPLOYEE COMPENSATION ANALYSIS

# In[1]:

import numpy as np
import pandas as pd
import os
import datetime


# In[2]:

# Read csv into a dataframe
df = pd.read_csv('Data/employee_compensation.csv') 


# ### Filter data by calendar year and find average salary for every employee.

# In[3]:

# Create a dataframe for calendar year
cal_df = df[df['Year Type'] == 'Calendar']
#Filter out the columns concerning employee salaries, compensation and benefits
cal_df = cal_df[['Employee Identifier', 'Salaries', 'Overtime', 'Other Salaries', 'Retirement', 'Health/Dental', 'Other Benefits']]
cal_df.head()


# In[4]:

# Calculating average salary and average benefits for each employee
cal_df['Average Salary'] = cal_df.apply(lambda x:(x['Salaries'] + x['Overtime'] + x['Other Salaries'])/3, axis=1)
cal_df['Average Benefits'] = cal_df.apply(lambda x:(x['Retirement'] + x['Health/Dental'] + x['Other Benefits'])/3, axis=1)


# In[5]:

# Listing the top 5 entries
print('Top 5 entries:\n')
print(cal_df.head()[['Employee Identifier','Average Salary', 'Average Benefits']])


#  ### Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)

# In[6]:

# Fetch the records of employees where the 'Overtime' value is graeter than 5% of the 'Salaries' value
overtime_df = cal_df[df['Overtime'] > 0.05 * df['Salaries']]
overtime_df = overtime_df[['Employee Identifier','Salaries', 'Overtime']]
print('Top 5 employees with Overtime salary greater than 5% of salary :\n')
print(overtime_df.sort_values('Overtime', ascending=False).head())


# ### For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value. Display the top 5 Job Families according to this percentage value using df.head()

# In[7]:

# Fetching the benfits and compensation corresponding to each Job Family
jobfam_df = df[['Job Family', 'Total Benefits', 'Total Compensation']]
jobfam_df.head()


# In[8]:

# Calculating the average benefits and compensation for each 'Job Family'
jobfam_df = jobfam_df.groupby('Job Family').agg({'Total Benefits':np.mean,'Total Compensation':np.mean})
jobfam_df.head()


# In[9]:

# Calculating the percentage of average total benefits to total compensation for each 'Job Family' and printing the top 5 entries
jobfam_df['Percentage'] = jobfam_df['Total Benefits'] / jobfam_df['Total Compensation'] * 100
print('Top 5 entries for percentage of Benefits to Compensation for each Job Family :\n')
print(jobfam_df.sort_values('Percentage', ascending=False).head())


# In[ ]:



