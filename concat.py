#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as mk


# In[15]:


Data=mk.DataFrame({'A':['A1','B1','C1'],
          'B':['A2','B2','C2']})

df=mk.DataFrame({'A':['A3','B3','C3'],
                 'B':['A4','B4','C4']})
dfr=mk.concat([Data,df],ignore_index=True)


# In[16]:


dfr


# In[17]:


dfc=mk.concat([Data,df],axis=1)
dfc


# In[14]:


# Sample DataFrames
import pandas as pd
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2']})

df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'],
                    'B': ['B3', 'B4', 'B5']})

# Concatenating along rows
result = pd.concat([df1, df2],ignore_index=True)
print("Concatenated DataFrame along rows:\n", result)


# In[18]:


# Sample DataFrames
df3 = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                    'D': ['D0', 'D1', 'D2']})

# Concatenating along columns
result_columns = pd.concat([df1, df3], axis=1)
print("Concatenated DataFrame along columns:\n", result_columns)


# In[ ]:




