#!/usr/bin/env python
# coding: utf-8

# # Zomato data analysis project

# ### importing libraries

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


from matplotlib.pyplot import xlabel, ylabel
plt.xlabel = xlabel
plt.ylabel = ylabel


# ### create dataframe

# In[4]:


data = pd.read_csv(r"C:\Users\Dell\Downloads\Zomato data .csv")


# In[5]:


data


# ### covert the datatype of column - rate

# In[5]:


def handlerate(value):
    value = str(value).split('/')
    value = value[0];
    return float(value)

data['rate'] = data['rate'].apply(handlerate)
print(data.head())


# In[6]:


data.info()


# ### what type of restaurant do the majority of customers order from?

# In[7]:


data.head(3)


# In[8]:


sns.countplot(x = 'listed_in(type)',data = data)
plt.xlabel = 'Type of restaurant'


# #### conclusion - majority of the restaurant falls in dinning category

# ### How many votes has each type of restaurant received from customers?

# In[9]:


data.head(2)


# In[10]:


data.groupby(['listed_in(type)'],as_index = False)['votes'].sum().sort_values(by = 'votes',ascending = False)


# In[16]:


import matplotlib.pyplot as plt

df = data.groupby(['listed_in(type)'], as_index=False)['votes'].sum().sort_values(by='votes', ascending=False)

plt.figure(figsize=(10,6)) 
plt.plot(df['listed_in(type)'], df['votes'], color="green", marker="o")

plt.xlabel("Type of Restaurant", color="red", fontsize=15)
plt.ylabel("Votes", color="red", fontsize=15)
plt.title("Votes by Restaurant Type", fontsize=15)

plt.xticks(rotation=90)  
plt.tight_layout()
plt.show()


# #### conclusion - dinning restuarant receive maximum votes 

# ### What are the ratings that the majority of restaurants have received?

# In[8]:


data.head(3)


# In[9]:


plt.hist(data['rate'],bins = 5)
plt.title("ratings disttribution")
plt.show()


# #### conclusion - the mejority restaurant receive ratings from 3.5 to 4

# ### zomato has observed that most couples order most of their food online. what is their average spending on each order?

# In[13]:


data.head(5)


# In[14]:


sns.countplot(x = 'approx_cost(for two people)',data = data)


# #### conclusion - the majority of couples prefer resturants with an approximate cost of 300 rs.

# ### Which mode (online or offline)has eceived the maximum ratings?

# In[10]:


data.head(6)


# In[11]:


plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order',y= 'rate',data = data)


# #### conclusion - offline order lower ratings in comaprison to online order

# ### Which type of resturant received more offline orders,so thet zomato can customers with some food orders?

# In[12]:


data.head(6)


# In[6]:


pivot_table = data.pivot_table(index = 'listed_in(type)',columns = 'online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivot_table , annot =True, cmap = 'YlGnBu',fmt='d')
plt.title('Heatmap')
plt.xlabel('online_order')
plt.ylabel('listed_in(type)')
plt.show()


# #### conclusion - dinning resturant primarily accept offline orders,whereas cafes receive online orders. This suggests that clients prefers order in person at resturant,but prefer online at cafes.

# ### ---End
