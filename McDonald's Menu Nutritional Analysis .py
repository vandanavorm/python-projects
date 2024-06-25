#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df=pd.read_csv("NutricalDataset.csv")

#exploratory data analysis
# In[3]:


df.head(4)


# In[4]:


#summary information 
df.info()


# In[7]:


df.isnull().sum()

as we can see there are no null values in the data set
# In[12]:


#summary statistics
df.describe()


# In[10]:


#distribution of calories
plt.figure(figsize=(10, 6))
sns.histplot(df['Calories'], kde=True)
plt.title('Calorie Distribution')
plt.xlabel('Calories')
plt.ylabel('Frequency')
plt.show()


# In[11]:


plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Calories'])
plt.title('Box Plot of Calories')
plt.xlabel('Calories')
plt.show()


# In[13]:


plt.figure(figsize=(10, 6))
sns.histplot(df['Total Fat'], kde=True, color='blue', label='Total Fat')
sns.histplot(df['Protein'], kde=True, color='green', label='Protein')
sns.histplot(df['Carbohydrates'], kde=True, color='red', label='Carbohydrates')
plt.title('Distribution of Nutritional Components')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()


# In[14]:


plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['Total Fat', 'Protein', 'Carbohydrates']])
plt.title('Box Plot of Nutritional Components')
plt.xlabel('Nutritional Components')
plt.ylabel('Value')
plt.show()


# In[16]:


# Correlation matrix
corr = df.corr()

# Heatmap of the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Nutritional Components')
plt.show()


# In[17]:


category_means = df.groupby('Category').mean()

# Bar plot for average calories by category
plt.figure(figsize=(12, 8))
category_means['Calories'].plot(kind='bar', color='skyblue')
plt.title('Average Calories by Category')
plt.xlabel('Category')
plt.ylabel('Average Calories')
plt.xticks(rotation=45)
plt.show()

#data visualization
# In[17]:


#  Nutritional Composition by Category
category_avg_nutrition = df.groupby('Category')[['Dietary Fiber', 'Total Fat', 'Protein', 'Carbohydrates']].mean()
category_avg_nutrition.plot(kind='bar', figsize=(10, 6))
plt.title('Average Nutritional Composition by Category')
plt.xlabel('Category')
plt.ylabel('Average Value')
plt.xticks(rotation=45)
plt.legend(title='Nutrient')
plt.show()


# In[5]:


# Distribution of Nutrients
nutrients = ['Total Fat', 'Saturated Fat', 'Cholesterol', 'Sodium', 'Carbohydrates', 'Protein']
df[nutrients].plot(kind='box', figsize=(10, 6))
plt.title('Distribution of Nutrients')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.show()


# In[25]:


# Comparison of Menu Items
burger_items = df[df['Category'] == 'Chicken & Fish']
burger_items[['Item', 'Protein', 'Total Fat','Carbohydrates']].set_index('Item').plot(kind='bar', figsize=(10, 10))
plt.title('Nutrient content of chicken & fish category')
plt.xlabel('Burger')
plt.ylabel('Value')
plt.xticks(rotation=90, ha='right')
plt.show()


# In[12]:


#  Daily Value Percentage Analysis
dv_nutrients = ['Total Fat (% Daily Value)', 'Saturated Fat (% Daily Value)', 
                'Cholesterol (% Daily Value)', 'Sodium (% Daily Value)',
                'Carbohydrates (% Daily Value)', 'Dietary Fiber (% Daily Value)']
df[dv_nutrients].plot(kind='hist', bins=10, alpha=0.7, figsize=(10, 6))
plt.title('Daily Value Percentage Distribution')
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.legend(title='Nutrient', loc='upper right')
plt.show()


# In[14]:


#Correlation nutrition Analysis
corr_matrix = df[['Calories', 'Total Fat', 'Saturated Fat', 'Cholesterol', 'Sodium', 'Carbohydrates', 'Protein']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Nutrients')
plt.show()


# In[15]:


#Nutrient Balance
nutrients_balance = df[['Total Fat', 'Saturated Fat', 'Cholesterol', 'Sodium', 'Carbohydrates', 'Protein']]
sns.pairplot(nutrients_balance)
plt.title('Nutrient Balance')
plt.show()


# In[29]:


#Comparison with Dietary Guidelines (Example: Calories)
plt.figure(figsize=(10, 6))
sns.histplot(df['Calories'], bins=20, kde=True, color='blue', alpha=0.5)
plt.axvline(x=450, color='red', linestyle='--', label='Recommended Calories Intake Per Meal')
plt.title('Calories Distribution vs. Recommended Calorie Intake Per Meal')
plt.xlabel('Calories')
plt.ylabel('Frequency')
plt.legend()
plt.show()

#nutritional insights
# In[31]:


# box plot for protein content by menu category
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Protein', data=df, palette='Set2')
plt.title('Protein Content Distribution by Menu Category')
plt.xlabel('Menu Category')
plt.ylabel('Protein (g)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[34]:


#top 10 highest calorie items
menu_data_sorted = df.sort_values(by='Calories', ascending=False)

top_10_high_calorie = menu_data_sorted.head(10)

top_10_low_calorie = menu_data_sorted.tail(10)


plt.figure(figsize=(10, 6))
plt.bar(top_10_high_calorie['Item'], top_10_high_calorie['Calories'], color='skyblue')
plt.xlabel('Calories')
plt.ylabel('Menu Item')
plt.title('Top 10 Menu Items by Calorie Count')
plt.xticks(rotation=90, fontsize='small')
plt.tight_layout()
plt.show()


# In[37]:


#top 10 lowest calorie items
menu_data_sorted = df.sort_values(by='Calories', ascending=False)


top_10_low_calorie = menu_data_sorted.tail(10)


plt.figure(figsize=(10, 6))
plt.bar(top_10_low_calorie['Item'], top_10_low_calorie['Calories'], color='skyblue')
plt.xlabel('Calories')
plt.ylabel('Menu Item')
plt.title('top_10_low_calorie')
plt.xticks(rotation=90, fontsize='small')
plt.tight_layout()
plt.show()


# In[39]:


#average nutritional content of popular menu categories

average_nutrition_by_category = df.groupby('Category')[['Calories', 'Total Fat', 'Protein', 'Carbohydrates']].mean()

popular_categories = df['Category'].value_counts().head(5).index  
# Assuming we're interested in the top 5 most popular categories

popular_categories_average_nutrition = average_nutrition_by_category.loc[popular_categories]
print(popular_categories_average_nutrition)


# In[ ]:




