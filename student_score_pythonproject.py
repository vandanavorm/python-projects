#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[6]:


df=pd.read_csv('student_score.csv')
df.head()


# In[22]:



df.describe()


# In[8]:


df.info()


# In[20]:


df.isnull().sum()


# In[25]:


#drop column unnamed
df=df.drop("Unnamed: 0",axis=1)
df.head()


# In[28]:


#change weekly study hour
#df["WklyStudyHours"]=df["Wkly#StudyHours"].str.replace("old value","new value")


# In[40]:


plt.figure(figsize=(5,5))

ax=sns.countplot(data=df,x='Gender')
ax.bar_label(ax.containers[0])
plt.show()


# In[41]:


#from above plot we have analysed that females are more than no.of males


# In[50]:


gb=df.groupby('ParentEduc').agg({'MathScore': 'mean',"ReadingScore":'mean',"WritingScore":'mean'})
gb


# In[58]:


sns.heatmap(gb,annot=True)
plt.show()


# In[59]:


#from above heatmap i concluded that parent's education impacts the kid's scores in a good way


# In[60]:


gb1=df.groupby('ParentMaritalStatus').agg({'MathScore': 'mean',"ReadingScore":'mean',"WritingScore":'mean'})
gb1


# In[62]:


sns.heatmap(gb1,annot=True)
plt.show


# In[63]:


#there is negligible impact of marital status of parents on kid


# In[69]:


gb2=df.groupby('PracticeSport').agg({'MathScore': 'mean',"ReadingScore":'mean',"WritingScore":'mean'})
gb2


# In[70]:


sns.heatmap(gb2,annot=True)


# In[66]:


#no impact


# In[71]:


sns.boxplot(data=df, x='MathScore')
plt.show()


# In[72]:


sns.boxplot(data=df, x='ReadingScore')
plt.show()


# In[73]:


sns.boxplot(data=df, x='WritingScore')
plt.show()


# In[74]:


df['EthnicGroup'].unique()


# In[92]:


groupa=df.loc[(df['EthnicGroup']=="group A")].count()
groupb=df.loc[(df['EthnicGroup']=="group B")].count()
groupc=df.loc[(df['EthnicGroup']=="group C")].count()
groupd=df.loc[(df['EthnicGroup']=="group D")].count()
groupe=df.loc[(df['EthnicGroup']=="group E")].count()


l=['group A','group B','group C','group D','group E']
mlist=[groupa['EthnicGroup'],groupb['EthnicGroup'],groupc['EthnicGroup'],groupd['EthnicGroup'],groupe['EthnicGroup']]
plt.pie(mlist,labels=l,autopct='%1.2f%%')
plt.show()


# In[96]:


ax=sns.countplot(data=df,x='EthnicGroup')
ax.bar_label(ax.containers[0])
plt.show


# In[ ]:




