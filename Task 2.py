#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


data = {'Product': ['Electronics', 'Clothing', 'Electronics', 'Electronics', 'Clothing'],
        'Region': ['North', 'South', 'East', 'West', 'North'],
        'Sales': [1000, 1500, 2000, 1200, 1800]}
data2=pd.DataFrame(data)
data2


# In[8]:


data2[(data2['Product'] == 'Electronics')]


# In[21]:


mean1=data2['Sales'].mean()
mean1


# In[33]:


ans=data2[data2['Sales']>mean1]
ans


# In[38]:


data2[(data2['Region']=='North') & (data2['Sales']<=1000)]


# In[ ]:




