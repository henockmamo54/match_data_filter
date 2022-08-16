#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd


# 1 Read data
# ===

# In[140]:


data=pd.read_csv("match_data.csv")
data["MatchYear"]=[y if y >2000 else y+2000 for y in  [ int(x.split('/')[2]) for x in data.MatchDate]] # format the match year, some of the data is 2022 and some of them are 22 only. this convers all to 2022 format
data.to_csv("test.csv")
data.head()


# 2 Methods
# ===

# In[146]:


def find_match(input_string):
    teams=input_string.strip().split(':')
    querystring=(f" (HomeTeam == '{teams[0].strip()}' and AwayTeam == '{teams[1].strip()}')                  or (HomeTeam == '{teams[1].strip()}' and AwayTeam == '{teams[0].strip()}') ")
    return data.query(querystring)

def find_match_per_year(input_string,year):
    data.MatchDate=data.MatchDate.astype(str)
    teams=input_string.strip().split(':')
    querystring=(f" ( (HomeTeam == '{teams[0].strip()}' and AwayTeam == '{teams[1].strip()}')                  or (HomeTeam == '{teams[1].strip()}' and AwayTeam == '{teams[0].strip()}') ) and                  MatchYear == {year}") 
    return data.query(querystring)

    
def find_match_by_country(country):
    return data.query(f"HomeTeam =='{country}' or AwayTeam == '{country}' ")


# 3 Examples
# ===

# <i>
# (1) If South Korea and Japan are given as input, then it finds the match South Korea: Japan or Japan: South Korea 
# (2) Furthermore, it does any match, for example, Japan: Qatar (or Qatar: Japan) and South Korea: Qatar (or Qatar: South Korea) in the same year.
# (3) The output gives the corresponding line (match date, home team, ...  Away team rating) that satisfies the conditions in (1) and (2).
#     </i>

# In[150]:


find_match("England:Hungary")


# In[151]:


find_match_per_year("England:Hungary",2022)


# In[152]:


find_match_by_country("South Korea")


# In[ ]:





# In[ ]:




