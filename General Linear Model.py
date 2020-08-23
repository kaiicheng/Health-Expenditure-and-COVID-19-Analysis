#!/usr/bin/env python
# coding: utf-8

# In[1]:


import statsmodels.api as sm
import pandas as pd
import numpy as np


# In[2]:


df = pd.read_excel("General Linear Model Data.xlsx")
df.head(15)


# In[3]:


df


# In[4]:


print(df['Country Name'])


# In[5]:


print(df['Case'])


# In[6]:


df['2017 Expen PPP']


# In[7]:


X = df['2017 Expen PPP']


# In[8]:


y = df['Case']


# In[9]:


X


# In[10]:


print(len(X))


# In[11]:


X = np.array(df['2017 Expen PPP(Rounded)'])


# In[12]:


X


# In[21]:


################
X = sm.add_constant(X, prepend=False)


# In[22]:


X


# In[ ]:





# In[15]:


y = np.array(df['Case'])


# In[16]:


y


# In[ ]:





# In[17]:


# Ordinary least square method.
mod = sm.OLS(y, X)


# In[18]:


res = mod.fit()


# In[19]:


print(res.summary())


# In[ ]:




