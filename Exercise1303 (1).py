#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.DataFrame({'Name':['Sam','Jack','Willam'],
   'Age':[31,26,30],
   'City':['New york','Washington','Cambridge']})
df


# In[2]:


df.loc[:, 'Name']


# In[3]:


df[(df['Age']>30)]


# In[4]:


df['Country'] = 'USA'
df


# In[5]:


df.sorted([])


# In[6]:


df.groupby('City')['Age'].mean()


# In[7]:


df.dropna()


# In[8]:


df1=pd.DataFrame({'City':['New york','Washington','Cambridge'],
                 'Population':[120000,250000,7500000]})
df1


# In[9]:


pd.merge(df,df1,on='City')


# In[ ]:





# In[ ]:




