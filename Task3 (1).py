#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


students={'Student_Id': [80, 65, 75, 90, 85],
         'Name': ['Alice', 'Bob', 'Charlie', 'john', 'Emily'], 
         'Grade': ['A', 'C', 'A', 'B', 'B'], 
         'Subject':['DS','SS','Maths','History','English']}
data3=pd.DataFrame(students)
data3


# In[7]:


data3[(data3['Grade']=='A') & (data3['Subject']=='Maths')]


# In[13]:


data3[(data3['Subject']=='History') | (data3['Subject']=='English') ]


# In[14]:


data3[(data3['Name']=='john')]


# In[ ]:




