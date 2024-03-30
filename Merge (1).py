#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.DataFrame({'Name_ Boys':['keerthan','Navani','Able','Ashwin','Sasi'],
                  'Marks_Boys':[56,76,87,89,90],
                  'Subject_code':['Sub10','Sub20','Sub30','Sub40','Sub50']})
data2=pd.DataFrame({'Name_ Girls':['keerthana','Navina','Anitha','Ashwini','Saranya'],
                  'Marks_Girls':[65,67,78,98,97],
                  'Subject_code':['Sub01','Sub20','Sub30','Sub40','Sub05']})


# In[5]:


pd.merge(data,data2,on='Subject_code') # Inner Join


# In[7]:


pd.merge(data,data2,on='Subject_code',how='left')#left join


# In[8]:


pd.merge(data,data2,on='Subject_code',how='right')#right join


# In[9]:


pd.merge(data,data2,on='Subject_code',how='outer')#full join


# In[ ]:




