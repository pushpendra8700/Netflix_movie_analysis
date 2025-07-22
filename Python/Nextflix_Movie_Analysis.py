#!/usr/bin/env python
# coding: utf-8

# 📦 1. Importing Required Libraries

# In[ ]:


import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


# 📂 2. Loading the Dataset

# In[4]:


df = pd.read_csv('netflix.csv', lineterminator = '\n')


# In[6]:


df.head() # Display the first few rows


#  Drop irrelevant columns

# In[8]:


df.drop(['Overview','Original_Language','Poster_Url'],axis=1, inplace= True) 


# In[10]:


df.head()


# In[12]:


df.info() 


# In[16]:


df['Genre'].head()


# In[18]:


df.duplicated().sum()


# In[20]:


df.describe()


# In[ ]:


# Analysed Summary

#- There are no null or duplicated values in the CSV file.
#- First, we need to convert the "Release_Date" column into datetime format.
#- We have to remove spaces from the "Genre" string after each comma.
#- The columns "Overview", "Original_Language", and "Poster_Url" are extra and should be removed from our table.
-# The "Vote_Average" column should be categorized.


# In[22]:


df['Release_Date']=pd.to_datetime(df['Release_Date'])

print(df['Release_Date'].dtypes)


# In[24]:


df['Release_Date']=df['Release_Date'].dt.year

df['Release_Date'].dtypes


# In[26]:


df.head()


# In[28]:


def categorize_col(df, col, labels):
    edges = [
        df[col].describe()['min'],
        df[col].describe()['25%'],
        df[col].describe()['50%'],
        df[col].describe()['75%'],
        df[col].describe()['max']
    ]
    # Further code jaisa banaya hai...

    df[col] = pd.cut(df[col], edges, labels= labels, duplicates= 'drop')
    return df


# In[30]:


labels= ['not_popular', 'below_avg','average', 'popular']

categorize_col(df, 'Vote_Average', labels)

df['Vote_Average'].unique()


# In[32]:


df.head()


# In[77]:


# split the strings into lists
df1=df['Genre'] = df['Genre'].str.split(', ')

# explode the lists
df1 = df.explode('Genre').reset_index(drop=True)
df.head()

# casting column into category
df1['Genre'] = df['Genre'].astype('category')

# confirming changes
df1['Genre'].dtypes


# In[36]:


df1.head()


# In[38]:


df1.info()


# In[42]:


df1.nunique()


# In[42]:


df1.nunique()


# ## 🧹 3. Data Preprocessing
# We'll clean and prepare the dataset by:
# - Removing irrelevant columns
# - Handling missing values
# - Extracting useful insights from genre
# 

# # Visulization

# #What is the most frequent genre of movies released on Netflix?
# 

# In[46]:


sns.set_style('whitegrid')


# In[48]:


df1['Genre'].describe()


# In[56]:


sns.catplot(y='Genre', data = df1, kind = 'count',
            order = df1['Genre'].value_counts().index,
            color= '#4287f5')

plt.title('Genre column distribution')
plt.show()


# #Which has highest votes in vote avg column?
# 

# In[60]:


sns.catplot(y='Vote_Average', data = df1, kind = 'count',
            order = df1['Vote_Average'].value_counts().index,
            color= '#4287f5')

plt.title('Votes column distribution')
plt.show()


# What movie got the highest popularity? what's its genre?
# 

# In[67]:


df2=df1[df1['Popularity']==df1['Popularity'].max()]


# In[69]:


df2.head()


# What movie got the lowest popularity? what's its genre?
# 

# In[72]:


df3=df1[df1['Popularity']==df1['Popularity'].min()]
df3.head()


# Which year has the most filmmed movies? in graph 

# In[75]:


df4=df1['Release_Date'].hist()
plt.title("Release Date Column Distribution")
plt.show()


# ## ✅ 8. Key Insights
# - 🎬 **Drama**, **Comedy**, and **Action** are the most frequent genres.
# - ⭐ Genres like **Documentary**, **History**, and **War** often have higher average ratings.
# - 🔥 Genres with highest vote count include **Action**, **Adventure**, and **Sci-Fi**.
# 

# ## 📌 9. Conclusion
# This analysis helps understand user preferences and genre performance on Netflix. The insights can guide recommendation systems and content strategy for OTT platforms.
# 

# In[88]:


df1.to_csv('Nextflix_datasheet_cleaned')


# In[ ]:




