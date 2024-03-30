#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


data = { 
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'], 
'Score': [80, 65, 75, 90, 85], 
'Salary': [50000, 60000, 55000, 70000, 65000], 
'Sales Amount': [300, 700, 400, 900, 600], 
'Grade': ['A', 'C', 'B', 'A', 'B'], 
'Book Title': ['Python Programming', 'Data Science Handbook', 
'Machine Learning Basics', 'Statistics in Python', 'Python for Beginners'], 
'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'San Francisco'], 
'Date': ['2023-01-05', '2023-02-10', '2022-12-15', '2023-03-20', '2023-01-01'], 
'Category': ['Electronics', 'Books', 'Electronics', 'Books', 'Electronics'] }
mdata=pd.DataFrame(data)
mdata


# In[5]:


index_data=mdata.iloc[0:4]
index_data


# In[6]:


score_data=mdata[(mdata['Score']<70)][['Name','Score']]
score_data


# In[7]:


name_column = mdata.loc[:, 'Name']
name_column


# In[8]:


sale_data=mdata[(mdata['Sales Amount']<500)][['Name','Sales Amount']]
sale_data


# In[9]:


row_data=mdata.iloc[0:2]
row_data


# In[10]:


Grade=mdata[(mdata['Grade']=='A') | (mdata['Grade']=='B')] [['Name','Grade']]
Grade


# In[11]:


python = mdata[(mdata['Book Title'].str.contains('Python'))] [['Book Title']]
python 


# In[12]:


cityname_data=mdata[(mdata['City']=='New York')][['City']]
cityname_data


# In[13]:


Date_data=mdata[(mdata['Date']<='2023-01-01')][['Date']]
Date_data


# In[14]:


cat_data=mdata[(mdata['Category']=='Electronics')][['Name','Category']]
cat_data


# In[ ]:


out=mdata[]

