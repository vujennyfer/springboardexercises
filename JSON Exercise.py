
# coding: utf-8

# JSON examples and exercise
# 
#     get familiar with packages for dealing with JSON
#     study examples with JSON strings and files
#     work on exercise to be completed and submitted
# 
#     reference: http://pandas.pydata.org/pandas-docs/stable/io.html#io-json-reader
#     data source: http://jsonstudio.com/resources/
# 

# In[3]:


import pandas as pd 
import json 
from pandas.io.json import json_normalize


# JSON example, with string
# 
#     demonstrates creation of normalized dataframes (tables) from nested json string
#     source: http://pandas.pydata.org/pandas-docs/stable/io.html#normalization
# 

# In[4]:


# define json string
data = [{'state': 'Florida', 
         'shortname': 'FL',
         'info': {'governor': 'Rick Scott'},
         'counties': [{'name': 'Dade', 'population': 12345},
                      {'name': 'Broward', 'population': 40000},
                      {'name': 'Palm Beach', 'population': 60000}]},
        {'state': 'Ohio',
         'shortname': 'OH',
         'info': {'governor': 'John Kasich'},
         'counties': [{'name': 'Summit', 'population': 1234},
                      {'name': 'Cuyahoga', 'population': 1337}]}]


# In[5]:


# use normalization to create tables from nested element
json_normalize(data, 'counties')


# In[6]:


# further populate tables created from nested element
json_normalize(data, 'counties', ['state', 'shortname', ['info', 'governor']])


# JSON example, with file
# 
#     demonstrates reading in a json file as a string and as a table
#     uses small sample file containing data about projects funded by the World Bank
#     data source: http://jsonstudio.com/resources/
# 

# In[7]:


# load json as string
json.load((open('C:/world_bank_projects_less.json')))


# In[8]:


# load as Pandas dataframe
sample_json_df = pd.read_json('C:/world_bank_projects_less.json')
sample_json_df


# JSON exercise
# 
# Using data in file 'data/world_bank_projects.json' and the techniques demonstrated above,
# 
#     1. Find the 10 countries with most projects
#     2. Find the top 10 major project themes (using column 'mjtheme_namecode')
#     3. In 2. above you will notice that some entries have only the code and the name is missing. Create a dataframe with the missing names filled in.
# 

# In[9]:


#QUESTION 1:

json_data = pd.read_json('C:/world_bank_projects.json')


# In[10]:


occurrences = json_data.groupby('countryname').countryname.count().reset_index(name="count")
occurrences.sort_values('count', ascending=False)
#Top ten countries are China, Indonesia, Vietnam, India, Yemen, Bangladesh, Nepal, Morocco, Mozambique, Burkina Faso


# In[11]:


#Question 2:

json_df = pd.read_json('C:/world_bank_projects.json')


# In[25]:


data = json.load((open('C:/world_bank_projects.json')))


# In[26]:


type(data)


# In[31]:


json_normalize(data, 'mjtheme_namecode', 'countryname')


# In[32]:


theme = json_normalize(data, 'mjtheme_namecode', 'countryname')
theme['name'].value_counts().head(10)
#The top 10 project themes are:
#1. Environment/Natural Resource Mgmt
#2. Rural Development
#3. Human Development
#4. Public Sector Governance
#5. Social Protection and Risk Mgmt
#6. Financial/Private Sector Development
#7. Social dev/gender/inclusion
#8. Trade and integration
#9. Urban Development
#10. Economic Management.
#Counts below:


# In[35]:


#QUESTION 3:
#Make a dict for thse values to map
dict = {'1': 'Economic Management', '2': 'Public Sector Governance', '3': 'Rule of Law', '4': 'Financial and Private Sector Development', '5':'Trade and Integration', '6':'Social Protection and Risk Management', '7':'Social dev/gender/inclusion', '8':'Human Development', '9': 'Urban Development', '10':'Rural Development', '11':'Environment/Natural Resource Management'}


# In[36]:


norm_json2 = norm_json
norm_json2['name'] = pd.Series()
idx = 0 
while idx < len(norm_json2):
    
    a = str(norm_json2.iloc[(idx), 0])
    #print(a)
    norm_json2.iloc[(idx), 1] = dict[a]
    idx += 1


# In[37]:


norm_json2

