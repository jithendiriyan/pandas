#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df1={'A':[1,2,33,None,45],
   'B':[12,None,56,66,55],
   'C':[35,25,15,None,75]}
df=pd.DataFrame(df1)
df


# In[26]:


mean=df['A'].mean()
mean


# In[28]:


df['A'].fillna(mean,inplace=True)


# In[34]:


median=df['B'].median()


# In[35]:


df['B'].fillna(median,inplace=True)


# In[38]:


mode=df['C'].mode()
df['C'].fillna(mode,inplace=True)


# In[39]:


df


# In[3]:


df.mean()


# In[ ]:




