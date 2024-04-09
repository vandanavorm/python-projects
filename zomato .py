#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


dfa=pd.read_csv('zomato.csv')
dfa.head()


# In[5]:


def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

dfa['rate']=dfa['rate'].apply(handleRate)
print(dfa.head())


# In[7]:


dfa.head()


# In[11]:


dfa.info()


# In[13]:



sns.countplot(x=dfa['listed_in(type)'])
plt.xlabel("type of restaurant")


# In[ ]:


#Conclusion: The majority of the restaurants fall into the dining category


# In[17]:


grouped_data = dfa.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c="green", marker="o")
plt.xlabel("Type of restaurant", c="red", size=20)
plt.ylabel("Votes", c="red", size=20)


# In[ ]:


#Conclusion: Dining restaurants are preferred by a larger number of individuals


# In[19]:


max_votes = dfa['votes'].max()
restaurant_with_max_votes = dfa.loc[dfa['votes'] == max_votes, 'name']
 
print("Restaurant(s) with the maximum votes:")
print(restaurant_with_max_votes)


# In[ ]:





# In[21]:


sns.countplot(x=dfa['online_order'])


# In[22]:


plt.hist(dfa['rate'],bins=5)
plt.title("Ratings Distribution")
plt.show()


# In[23]:


couple_data=dfa['approx_cost(for two people)']
sns.countplot(x=couple_data)


# In[25]:


plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = dfa)


# In[26]:


pivot_table = dfa.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()


# In[ ]:




