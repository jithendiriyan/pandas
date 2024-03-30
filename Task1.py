#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[18]:


data = { 
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Saranya'],
    'age':[45,28,27,33,34],
    'Gender':['male','male','male','male','female'],
    'Salary': [50000, 60000, 55000, 70000, 65000], 
}
data1=pd.DataFrame(data)
data1


# In[28]:


data1.loc[data1['age'] > 30, ['Name', 'age']]


# In[20]:


data1[(data1['Gender'] == 'male') & (data1['Salary'] > 50000)]


# In[24]:


data1[(data1['Name'].str.startswith('S'))]


# In[ ]:





# In[ ]:





# In[ ]:




