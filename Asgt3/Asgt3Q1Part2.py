
# coding: utf-8

# ## NYC Collision Analysis - Part 2

# ### For each borough, find out distribution of collision scale. (One car involved? Two? Three? or more?) (From 2015 to present)

# In[1]:

import numpy as np
import pandas as pd
import os
import datetime


# In[2]:

# Read collision data from csv into a dataframe
df = pd.read_csv('Data/vehicle_collisions.csv', index_col = 3) 
df.head()


# In[3]:

# Creating dataframe with relevant columns conaining the Boroughs and the vehicles involved during collisions for each borough.
df = df[['VEHICLE 1 TYPE', 'VEHICLE 2 TYPE', 'VEHICLE 3 TYPE', 'VEHICLE 4 TYPE', 'VEHICLE 5 TYPE']]
df.head()


# In[4]:

# Summing up the number of vehicles for each row
df['TOTAL_VEHICLES'] = df.notnull().sum(axis=1)
df.head()


# In[5]:

df = df.reset_index()[['BOROUGH','TOTAL_VEHICLES']]
df.head()


# In[6]:

# Creating a pivot table to aggregate the number of collisions for each borough with respect to number of vehicles involved
df = df.pivot_table(index='BOROUGH', columns='TOTAL_VEHICLES', aggfunc=len, fill_value=0)
df = df.rename(index=str, columns={0:"NO_VEHICLE_INVOLVED", 1:"ONE_VEHICLE_INVOLVED", 2:"TWO_VEHICLES_INVOLVED", 3:"THREE_VEHICLES_INVOLVED",4:"FOUR_VEHICLES_INVOLVED",5:"FIVE_VEHICLES_INVOLVED"})


# In[7]:

df


# In[8]:

os.makedirs('Output', exist_ok=True)


# In[9]:

df.to_csv('Output/Q1Part2.csv')


# In[10]:

print('Completed the analysis for calculating the distribution of collision scale to show the number of vehicles involved for each collision on each borough. Output is saved as a csv file in the location Output/Q1Part2.csv')


# In[ ]:



