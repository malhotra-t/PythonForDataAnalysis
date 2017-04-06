
# coding: utf-8

# ## CRICKET MATCHES ANALYSIS

# ### Calculate the average score for each team which host game and win game.

# In[10]:

import numpy as np
import pandas as pd
import os
import datetime


# In[11]:

# Read csv into dataframe
df = pd.read_csv('Data/cricket_matches.csv') 


# In[12]:

df = df[['home', 'away', 'winner', 'innings1', 'innings2', 'innings1_runs', 'innings2_runs']]
# Check if the winning team was the host team as well
df = df[df['home'] == df['winner']]


# In[13]:

# Check if the winning host team played innings 1 or innings 2
df['winner_runs'] = df.apply(lambda x:x['innings1_runs'] if x['innings1'] == x['home'] else x['innings2_runs'], axis = 1)


# In[14]:

# Group the winning host teams from the above step to find the average score
df = df.groupby('home').agg({'winner_runs':np.mean})
print('Top 5 average scores of teams which won as a host team is shown below:\n')
print(df.sort_values('winner_runs',ascending=False).head())


# In[15]:

os.makedirs('Output', exist_ok=True)


# In[16]:

df.to_csv('Output/Q3Part1.csv')


# In[17]:

print('Completed the cricket match analysis to determine average scores of top 5 winning host teams. The results have been saved in Output/Q3Part1.csv')


# In[ ]:



