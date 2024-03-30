#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data={'Name':["Jeeva","venky","Karthi","Abith","jeevankumar"],
     'Age':[23, 24, 25, 22, None],
     'City':['Gobi','Avinashi','Kurumathur','kaniyakumari',None]}
data1=pd.DataFrame(data)
data1


# In[3]:


data1.isnull()


# In[4]:


data1.isnull().sum()


# In[5]:


data1.info()


# In[6]:


data1.describe()


# In[7]:


data1.head(3)


# In[8]:


data1.tail(2)


# In[9]:


data1.sample(3)


# In[10]:


data1.dropna()


# In[14]:


data1.fillna(12)


# In[15]:


data1.fillna('nambiyur')


# In[16]:


data1.bfill()


# In[17]:


data1.ffill()


# In[18]:


data1.fillna({'Age':25,'City':'Nambiyur'})


# In[19]:


data1


# In[20]:


data1.fillna({'Age':25,'City':'Nambiyur'},inplace=True)
data1


# In[21]:


data1


# In[24]:


data1.duplicated()


# In[23]:


data1


# In[33]:


data1.duplicated()


# In[34]:


import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
        'Age': [25, 30, 25, 22, 28]}

df = pd.DataFrame(data)


# In[35]:


df


# In[36]:


df.duplicated()


# In[39]:


df.drop_duplicates()


# In[44]:


data3 = pd.read_excel('E:\excelsample.xlsx')
data3


# In[45]:


data3.isnull()


# In[48]:


data3.fillna('europe',inplace=True)


# In[49]:


data3


# In[ ]:





# In[ ]:




