#!/usr/bin/env python
# coding: utf-8

# # Seaborn Visualization Library

# In[10]:


import pandas as pd
ds=pd.read_csv('emptest.csv')
print(ds)
print(ds.head())


# In[17]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


sns.violinplot(x='Age',data=ds)


# In[5]:


sns.violinplot(x='Salary',data=ds)


# In[6]:


sns.swarmplot(x='Salary',data=ds)


# In[7]:


sns.countplot(x='Salary',data=ds)


# In[8]:


sns.stripplot(x='Salary',data=ds)


# In[9]:


sns.catplot(x='Salary',data=ds)


# # IRIS FLOWER DATASET

# In[18]:


dsiris=pd.read_csv('Iris.csv')
print(dsiris)
print(dsiris.head())
sns.set(style='whitegrid')
ax=sns.stripplot(x='class', y='sepal length', data=dsiris)
plt.title('Graph')
plt.show()


# In[19]:


ax=sns.swarmplot(x='class', y='sepal length', data=dsiris)
plt.title('Graph')
plt.show()


# In[26]:


dsiris['class'].value_counts()


# In[27]:


sns.countplot(dsiris['class'])


# In[28]:


sns.get_dataset_names()


# In[29]:


titanicds=sns.load_dataset('titanic')
print(titanicds)


# In[31]:


titanicds.columns


# In[33]:


titanicds['class']


# In[34]:


titanicds['class'].value_counts()


# In[35]:


sns.countplot(titanicds['class'])


# In[36]:


g=sns.catplot(x='class',y='survived',hue='sex', data=titanicds,kind='bar')
plt.show()


# In[37]:


g=sns.catplot(x='class',y='survived',hue='sex', data=titanicds,kind='violin')
plt.show()


# In[39]:


sns.load_dataset('tips')


# In[43]:


tips=sns.load_dataset('tips')
print(tips.head())
sns.violinplot(x='total_bill',data=tips)
plt.show()


# In[45]:


sns.histplot(x='total_bill',data=tips, bins=20)


# In[48]:


sns.displot(tips['tip'], bins=10)


# In[50]:


sns.distplot(tips['total_bill'])


# In[51]:


sns.distplot(tips['total_bill'],bins=100)


# In[52]:


#kde-Kernel Density Extimation
sns.distplot(tips['total_bill'],bins=50, kde=False)


# In[53]:


sns.kdeplot(tips['total_bill'])


# In[ ]:




