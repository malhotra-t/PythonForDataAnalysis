
# coding: utf-8

# ## MOVIE AWARDS ANALYSIS

# In[1]:

import numpy as np
import pandas as pd
import os
import datetime
import re


# In[2]:

# Read movie_awards csv into a dataframe
df = pd.read_csv('Data/movies_awards.csv') 
df = df[['Title', 'Year', 'Awards']]


# In[3]:

# Pull out data from Awards column
df = df[pd.notnull(df['Awards'])]
df.head()


# In[4]:

# Regula exp to catch groups for finding special awards and nominations as well as simple awards and nominations
regex_pattern = re.compile('^((Won? (\d+) (\w*(\s\w*)*)( & )?)?(Nominated for? (\d+) (\w*(\s\w*)*))?\u002e\s?)?((Another )?(((\d+) win\w?)( & )?)?((\d+) nomination\w?)?\u002e)?$')


# In[5]:

# Function that is applied on each row to extract new columns for award and nomination counts
def awards_nom(row):
    match_result = regex_pattern.match(row['Awards'])
    if match_result:
        award_wins = match_result.group(3)
        award_type = match_result.group(4)
        if award_wins and award_type:
            if award_type[-1] == 's':
                award_type = award_type[:-1]
            award_type = award_type + ' Awards_Won'
            row[award_type] = award_wins

        award_nomination = match_result.group(8)
        nomination_type = match_result.group(9)
        if award_nomination and nomination_type:
            if nomination_type[-1] == 's':
                nomination_type = nomination_type[:-1]
            nomination_type = nomination_type + ' Awards_Nominated'
            row[nomination_type] = award_nomination

        simple_award_wins = match_result.group(15)
        if simple_award_wins:
            row['Awards_Won'] = simple_award_wins
            if award_wins:
                row['Awards_Won'] = int(row['Awards_Won']) + int(award_wins)

        simple_nom = match_result.group(18)
        if simple_nom:
            row['Awards_Nominated'] = simple_nom
            if award_nomination:
                row['Awards_Nominated'] = int(row['Awards_Nominated']) + int(award_nomination)
    return row  


# In[6]:

# Apply the funtion above on axis=1
df = df.apply(awards_nom,axis=1)
# Fill NaNs with 0
df = df.fillna(0)
df.head()


# In[7]:

os.makedirs('Output', exist_ok=True)


# In[8]:

df.to_csv('Output/Q4.csv')


# In[9]:

print('Results saved in Output/Q4.csv')


# In[ ]:



