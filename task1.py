#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[3]:


df=pd.read_excel('quantium.xlsx')
df.head()


# In[4]:


df.info


# In[5]:


df.describe()


# In[103]:


#brand wise total sales
x=df.groupby('LIFESTAGE')['TOT_SALES'].sum()

plt.figure(figsize=(6,4))
brand_sales.plot(kind='bar',color='black')
plt.title('SALES DISTRIBUTION BY BRAND')
plt.xlabel('BRAND')
plt.ylabel('TOTAL SALES')
plt.xticks(rotation=90)
plt.show


# conclusion: The sales data reveals that Kettle emerges as the top-selling chip brand, followed closely by Tostitos and Thins in sequence. This hierarchy underscores the prominence of Kettle in chip sales, with Tostitos and Thins following suit as significant contributors to overall sales figures.

# In[105]:


#lifestage wise sales

lifestage_dist=df.groupby('LIFESTAGE')['TOT_SALES'].sum()
lifestage_dist


# In[216]:


#avg sale per customer segment and lifestage wise
average_chip_price = df.groupby(['LIFESTAGE', 'PREMIUM_CUSTOMER'])['TOT_SALES'].sum() / df.groupby(['LIFESTAGE', 'PREMIUM_CUSTOMER'])['CHIP_QUANTITY'].sum()


plt.figure(figsize=(12, 6))
average_chip_price.unstack().plot(kind='bar')


plt.title('Average Chip Price by Customer Segment and Lifestage')
plt.xlabel('Lifestage')
plt.ylabel('Average Chip Price')


plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# In[73]:


#sales distribution in lifestage of customer

lifestage_dist=df.groupby('LIFESTAGE')['TOT_SALES'].sum()


plt.figure(figsize=(5,5))
lifestage_dist.plot(kind='pie')
plt.title('Total Sales by customer lifestage')

plt.show


# conclusion: Based on the data analysis, it's evident that retirees and old couples/singles contribute significantly to our sales, emerging as the largest contributors. This finding underscores the importance of targeting and catering to the needs and preferences of these demographic segments to optimize sales performance.

# In[80]:


#customer count under lifestage

lifestage_count=df['LIFESTAGE'].value_counts()
lifestage_count


# In[100]:


lifestage_count.plot(kind='bar' ,color='black')
plt.title('Distribution of Customers by Lifestage')
plt.xlabel('LIFESTAGE',fontsize='large')
plt.ylabel('NO. OF CUSTOMERS',fontsize='large')
plt.xticks( fontsize='small')

plt.show


# The analysis reveals that among the lifestage categories, Young Singles/Couples exhibit the highest count of 260 customers, followed by Retirees with 184 customers, and Older Singles/Couples with 174 customers, respectively.
# 
# In terms of total sales contribution by lifestage, Young Singles/Couples lead with  1443.0,closely followed by older singles/couples with 1440.9, and Retirees with $1417.1. This underscores the significant presence and purchasing power of these lifestage segments within the customer base.
# 
# ​

# In[178]:


#customer count over segment
plt.figure(figsize=(5,5))

ax=sns.countplot(data=df,x='PREMIUM_CUSTOMER')
ax.bar_label(ax.containers[0])
plt.show()


# the plot above tells the customer belonging to mainstream segment are highest in number followed by bugdet and premium

# In[183]:


#segment wise distribution of sales

segment_dist=df.groupby('PREMIUM_CUSTOMER')['TOT_SALES'].sum()

plt.figure(figsize=(5,4))
ax=segment_dist.plot(kind='bar',color='black')
plt.xlabel('CUSTOMER SEGMENT')
plt.ylabel('SALES')
ax.bar_label(ax.containers[0])
plt.xticks(rotation=0, fontsize='small')


# In[128]:


#count of customer by mainstream(customer segment)


# In[155]:


mainstream_dist = df[df['PREMIUM_CUSTOMER'] == 'Mainstream'].groupby('LIFESTAGE')['PREMIUM_CUSTOMER'].count()


mainstream_dist.plot(kind='pie')

plt.title('Distribution of Customers According to Lifestage Segment Wise',loc='left')
plt.ylabel('')
plt.show()


# In[207]:


#no. of pack sold packsize wise

plt.figure(figsize=(10,4))
ax=sns.countplot(data=df,x='pack_size')
ax.bar_label(ax.containers[0])
plt.title('pack wise sales')
plt.ylabel('sales')
plt.xlabel('pack size')
plt.xticks(rotation=90, fontsize='small')
plt.show()


# Following the plot analysis, it is evident that the 175g pack emerges as the top-selling variant in number of pack sold, closely followed by the 150g and 170g packs, respectively.

# In[206]:


packsize_sales= df.groupby('pack_size')['TOT_SALES'].sum()

plt.figure(figsize=(10,4))
ax=packsize_sales.plot(kind='bar',color='black')
plt.xlabel('PACK SIZE')
plt.ylabel('SALES')
ax.bar_label(ax.containers[0])
plt.xticks(rotation=90, fontsize='small')
plt.show()


# Following the plot analysis, it is evident that the 175g pack emerges as the top-selling variant , closely followed by the 150g and 300g packs, respectively.

# In[ ]:




