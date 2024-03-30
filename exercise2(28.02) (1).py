#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[10]:


sales_data=pd.read_excel('E:\excelsample2.xlsx')


# In[23]:


sales_data.drop_duplicates(keep='first',inplace=True)
sales_data


# In[ ]:




