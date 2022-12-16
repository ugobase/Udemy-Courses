#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Read the file

# In[2]:


#Read csv file
Don = pd.read_csv('udemy_courses.csv')


# # Get the first and last five rows of the csv file

# In[3]:


#First five rows of file
Don.head()


# In[4]:


#Last five rows of file
Don.tail()


# # How many rows and columns does the file have?

# In[5]:


#Number of rows
Don.shape[0]


# In[6]:


#Number of columns
Don.shape[1]


# In[7]:


Don.shape


# # Get the datatypes of the file

# In[8]:


#Datatypes
Don.dtypes


# In[9]:


#Info to know number of rows, columns, datatypes,null values
Don.info()


# In[10]:


#Checking for missing values
Don.isnull().sum()


# In[11]:


#Statistical description of data
Don.describe()


# In[12]:


#Cummulative sum of data
Don.cumsum


# In[13]:


#Maximum value in each column
Don.max()


# In[14]:


#Minimum value in each column
Don.min()


# In[15]:


#Time changed to regular time
Don['published_timestamp'] = pd.to_datetime(Don['published_timestamp'])
Don


# In[16]:


#Alternative to previous
Don.published_timestamp = pd.to_datetime(Don.published_timestamp)
Don


# In[17]:


#Counts of values in each year
Don['published_timestamp'].dt.year.value_counts()


# In[18]:


#Alternative to previous
Don.published_timestamp.dt.year.value_counts()


# In[19]:


#All years and indexes
Don.published_timestamp.dt.year


# In[20]:


#Counts of all values
Don.published_timestamp.dt.year.count()


# In[21]:


#Counts of values in each month
Don.published_timestamp.dt.month.value_counts()


# In[22]:


#Counts of values in each day
Don.published_timestamp.dt.day.value_counts()


# In[23]:


#Number of counts of 2017
Don[Don.published_timestamp.dt.year == 2017].shape[0]


# In[24]:


#Subjects and numbers published in 2017
Don[Don.published_timestamp.dt.year == 2017].subject.value_counts()


# In[25]:


#Top 5 selling courses
Don.nlargest(5, ['num_subscribers'])


# In[26]:


#Alternative to previous
Don.sort_values('num_subscribers', ascending = False).head()


# In[27]:


#Least 5 selling courses
Don.nsmallest(5, ['num_subscribers'])


# In[28]:


#Alternative to previous
Don.sort_values('num_subscribers').head()


# In[29]:


#Courses without any subscribers
Don[Don.num_subscribers== 0].shape[0]


# In[30]:


#All course_title that contains python
Don[Don['course_title'].str.contains('Python')].course_title


# In[31]:


Don[Don.course_title.str.contains('Python')].course_title


# In[32]:


#Show all courses that are free
Don[Don.is_paid == False].course_title


# In[33]:


#Show all courses that are paid
Don[Don.is_paid == True].course_title


# In[34]:


#Top 7 largest values of Price
Don.nlargest(n=7, columns=['price'])


# In[35]:


#Alternative to previous
Don.sort_values('price', ascending = False).head(7)


# In[36]:


#Top 10 largest values of num_subscribers
Don.nlargest(n=10, columns=['num_subscribers'])


# In[37]:


#Alternative to previous
Don.sort_values('num_subscribers', ascending = False).head(10)


# In[38]:


#Top 10 smallest values of price
Don.nsmallest(10, ['price'])


# In[39]:


#Alternative to previous
Don.sort_values('price', ascending = True).head(10)


# In[40]:


#Mean value of num_reviews
Don['num_reviews'].mean()


# In[41]:


#Names of unique values in level
Don.level.unique()


# In[42]:


#Number of All Levels in the level column
Don.loc[(Don['level'] == 'All Levels'), 'level']


# In[43]:


#Alternative to previous
Don[Don.level == 'All Levels'].level


# In[44]:


#Number of Expert level
Don.loc[(Don['level'] == 'Expert Level')].shape[0]


# In[45]:


#Alternative to previous
Don[Don.level == 'Expert Level'].value_counts().shape[0]


# In[46]:


Don[Don.level == 'Expert Level'].shape[0]


# In[47]:


#Value of price >= 45 and num_reviews >= 48
Don.loc[(Don['price'] >= 45) & (Don['num_reviews'] >= 48)].shape[0]


# In[48]:

#Alternative to previous
Don[(Don['price'] >= 45) & (Don['num_reviews'] >= 48)].shape[0]


# In[49]:

#Alternative to previous
Don[(Don.price >= 45) & (Don.num_reviews >= 48)].shape[0]


# In[50]:

#Number of reviews >=500 and number of subscribers >= 1000
Don[(Don['num_reviews'] >= 500) & (Don['num_subscribers'] >= 1000)].shape[0]


# In[51]:

#Alternative to previous
Don[(Don.num_reviews >= 500) & (Don.num_subscribers >= 1000)].shape[0]


# In[52]:


#Mean value of price >= 45 and num_reviews >=48
Don.loc[(Don['price'] >= 45) & (Don['num_reviews'] >= 48)].mean()


# In[53]:


#Value of num_lectures >= 274 or subject = web development
Don.loc[(Don['num_lectures'] >= 274) | (Don['subject'] == 'web development')].shape[0]


# In[54]:


#Alternative to previous
Don[(Don['num_lectures'] >= 274) | (Don['subject'] == 'web development')].shape[0]


# In[55]:

#Alternative to previous
Don[(Don.num_lectures >= 274) | (Don.subject == 'web development')].shape[0]


# In[56]:


#Number of unique values in the subject column
len(Don['subject'].unique())


# In[57]:


#Alternative to previous
Don['subject'].nunique()


# In[58]:

#Alternative to previous
Don.subject.nunique()


# In[59]:


#All unique values in the subject column
Don['subject'].unique()


# In[60]:


#Statistical description of the num_lectures column
Don['num_lectures'].describe()


# In[61]:


#Count of the subject column
Don['subject'].value_counts()


# In[62]:


#Show records where levels is All Levels or Intermediate Level
Don[Don['level'].isin(['All Levels', 'Intermediate Level'])]


# In[63]:

#Alternative to previous
Don[Don.level.isin(['All Levels', 'Intermediate Level'])]


# In[64]:


#20% increment of content_duration >= 39
Don.loc[(Don['content_duration'] >= 39), 'content_duration'] *1.2


# In[65]:


#Num_reviews increased by 5
Don['num_reviews'] = Don.num_reviews.apply(lambda x: x+5)
Don


# In[66]:


#Number of subscribers on intermediate level
Don.loc[(Don['level'] == 'Intermediate Level')].groupby(['num_subscribers']).count().shape[0]


# In[67]:


#Alternative to previous
Don[Don.level == 'Intermediate Level'].num_subscribers.value_counts().shape[0]


# In[68]:


#Number of subscribers that take graphic design
Don.loc[(Don['subject'] == 'Graphic Design')].groupby(['num_subscribers']).count().shape[0]


# In[69]:


#Alternative to previous
Don[Don.subject == 'Graphic Design'].num_subscribers.value_counts().shape[0]


# In[70]:


#unique values of is_paid
Don['is_paid'].unique()


# In[71]:


#is_paid is True and subject is business finance
Don.loc[(Don['is_paid'] == True) & (Don['subject'] == 'Business Finance')]


# In[72]:

#Histogram plot of price
ax = Don['price'].plot(kind = 'hist', figsize = (8,6))
ax.set_ylabel ('Next')
ax.set_xlabel ('Band')
plt.title('Don', loc = 'right')


# In[73]:

#Alternative to previous using seaborn
plt.figure(figsize=(12,8))
sns.histplot(Don['price'])


# In[74]:

#Box plot of number of lectures
ax = Don['num_lectures'].plot(kind = 'box', figsize = (8,6))
ax.set_ylabel ('Number of Sales')
plt.title('Don', loc = 'right')


# In[75]:

#Alternative to previous using seaborn
plt.figure(figsize=(12,8))
sns.boxplot(Don.num_lectures)


# In[76]:

#Density plot of number of reviews
ax = Don['num_reviews'].plot(kind = 'density', figsize = (8,6))
ax.set_ylabel ('Number of Sales')
ax.set_xlabel ('Dollars')
plt.title('Don', loc = 'right')


# In[77]:

#Alternative to previous using seaborn
plt.figure(figsize=(12,8))
sns.displot(Don.num_reviews, kind = 'kde')


# In[78]:

#Pie plot of level
Don['level'].value_counts().plot(kind = 'pie', figsize = (6,6))


# In[79]:

#Pie plot of subject
Don.subject.value_counts().plot(kind = 'pie', figsize = (6,6))


# In[80]:

#Bar chart of level
Don['level'].value_counts().plot(kind = 'bar', figsize = (6,6))


# In[81]:

#Counting levels
Don['level'].value_counts()


# In[82]:

#Correlation of the data
plt.figure(figsize = (10,5))
sns.heatmap(Don.corr(), annot = True, fmt = '0.1f')


# In[83]:

#Count plot of level
sns.countplot(Don['level'])


# In[84]:

#Count plot of subject
sns.countplot(Don.subject)


# In[85]:

#Box plot between subject against number of subscribers
plt.figure(figsize=(12,8))
sns.boxplot(data = Don, x = 'subject', y = 'num_subscribers')


# In[ ]:




