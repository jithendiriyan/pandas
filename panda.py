#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


s=Series.pd([1,3,4])
s


# In[3]:


s=pd.Series([1,2,3])
s


# In[5]:


dt=pd.DataFrame([[2,4,6],[1,3,5],[8,10,12]])
dt


# In[18]:


dt.iloc[0:][:1]


# In[24]:


dt1={'names':['Karthik','Arun','Sam'],
    'marks':[78,45,34]}
dt1 = pd.DataFrame(dt1)
dt1


# In[29]:


to={'name':['Karthi','sasi','jeevan','jp'],
   'Marks':[89,98,78,89],
   'age':[23,21,22,24]}
cto=pd.DataFrame(to)
cto


# In[35]:


to[(to['Marks'] > 85) & (to['name'] == 'jeevan')]


# In[ ]:





# In[ ]:




