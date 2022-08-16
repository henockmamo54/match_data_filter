#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd


# 1 Read data
# ===

# In[27]:


data=pd.read_csv("revised match data.csv")
data["MatchYear"]=[y if y >2000 else y+2000 for y in  [ int(x.split('/')[2]) for x in data.MatchDate]] # format the match year, some of the data is 2022 and some of them are 22 only. this convers all to 2022 format
data.to_csv("test.csv")
data.head()


# 2 Methods
# ===

# In[28]:


def find_match(input_string):
    teams=input_string.strip().split(':')
    querystring=(f" (HomeTeam == '{teams[0].strip()}' and AwayTeam == '{teams[1].strip()}')                  or (HomeTeam == '{teams[1].strip()}' and AwayTeam == '{teams[0].strip()}') ")
    return data.query(querystring)

def find_match_per_year(input_string,year):
    data.MatchDate=data.MatchDate.astype(str)
    teams=input_string.strip().split(':')
    querystring=(f" ( (HomeTeam == '{teams[0].strip()}' and AwayTeam == '{teams[1].strip()}')                  or (HomeTeam == '{teams[1].strip()}' and AwayTeam == '{teams[0].strip()}') ) and                  MatchYear == {year}") 
    return data.query(querystring)


def find_match_per_year_percountries(input_string1,input_string2,year):
    data.MatchDate=data.MatchDate.astype(str)
    teams1=input_string1.strip().split(':')
    teams2=input_string2.strip().split(':')
    
    querystring1=(f" ( (HomeTeam == '{teams1[0].strip()}' and AwayTeam == '{teams1[1].strip()}')                  or (HomeTeam == '{teams1[1].strip()}' and AwayTeam == '{teams1[0].strip()}') ) and                  MatchYear == {year}") 
    querystring2=(f" ( (HomeTeam == '{teams2[0].strip()}' and AwayTeam == '{teams2[1].strip()}')                  or (HomeTeam == '{teams2[1].strip()}' and AwayTeam == '{teams2[0].strip()}') ) and                  MatchYear == {year}") 
    data1=data.query(querystring1)
    data2=data.query(querystring2)
    
    return pd.concat([data1,data2])


    
def find_match_by_country(country):
    return data.query(f"HomeTeam =='{country}' or AwayTeam == '{country}' ")


def find_match_by_country_per_year(country,year):
    return data.query(f" (HomeTeam =='{country}' or AwayTeam == '{country}') and MatchYear == {year} ")


# 3 Examples
# ===

# <i>
# (1) If South Korea and Japan are given as input, then it finds the match South Korea: Japan or Japan: South Korea 
# (2) Furthermore, it does any match, for example, Japan: Qatar (or Qatar: Japan) and South Korea: Qatar (or Qatar: South Korea) in the same year.
# (3) The output gives the corresponding line (match date, home team, ...  Away team rating) that satisfies the conditions in (1) and (2).
#     </i>

# In[29]:


find_match("Japan: Qatar")


# <i>
#     filters the match between two countries on a specific year.
#     </i>

# In[30]:


find_match_per_year("South Korea: Qatar",2019)


# In[31]:


find_match_per_year_percountries("South Korea: Qatar","Japan: Qatar",2019)


# <i>
#     filters the match between per country
#     </i>

# In[32]:


find_match_by_country_per_year("South Korea",2022)


# In[33]:


find_match_by_country("South Korea")


# In[ ]:





# In[ ]:




