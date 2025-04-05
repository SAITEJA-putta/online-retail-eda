#!/usr/bin/env python
# coding: utf-8

# # Portfolio Project: Online Retail Exploratory Data Analysis with Python

# ## Overview
# 
# In this project, you will step into the shoes of an entry-level data analyst at an online retail company, helping interpret real-world data to help make a key business decision.

# ## Case Study
# In this project, you will be working with transactional data from an online retail store. The dataset contains information about customer purchases, including product details, quantities, prices, and timestamps. Your task is to explore and analyze this dataset to gain insights into the store's sales trends, customer behavior, and popular products. 
# 
# By conducting exploratory data analysis, you will identify patterns, outliers, and correlations in the data, allowing you to make data-driven decisions and recommendations to optimize the store's operations and improve customer satisfaction. Through visualizations and statistical analysis, you will uncover key trends, such as the busiest sales months, best-selling products, and the store's most valuable customers. Ultimately, this project aims to provide actionable insights that can drive strategic business decisions and enhance the store's overall performance in the competitive online retail market.
# 
# ## Prerequisites
# 
# Before starting this project, you should have some basic knowledge of Python programming and Pandas. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - numpy
# - seaborn
# - matplotlib
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`

# ## Project Objectives
# 1. Describe data to answer key questions to uncover insights
# 2. Gain valuable insights that will help improve online retail performance
# 3. Provide analytic insights and data-driven recommendations

# ## Dataset
# 
# The dataset you will be working with is the "Online Retail" dataset. It contains transactional data of an online retail store from 2010 to 2011. The dataset is available as a .xlsx file named `Online Retail.xlsx`. This data file is already included in the Coursera Jupyter Notebook environment, however if you are working off-platform it can also be downloaded [here](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx).
# 
# The dataset contains the following columns:
# 
# - InvoiceNo: Invoice number of the transaction
# - StockCode: Unique code of the product
# - Description: Description of the product
# - Quantity: Quantity of the product in the transaction
# - InvoiceDate: Date and time of the transaction
# - UnitPrice: Unit price of the product
# - CustomerID: Unique identifier of the customer
# - Country: Country where the transaction occurred

# ## Tasks
# 
# You may explore this dataset in any way you would like - however if you'd like some help getting started, here are a few ideas:
# 
# 1. Load the dataset into a Pandas DataFrame and display the first few rows to get an overview of the data.
# 2. Perform data cleaning by handling missing values, if any, and removing any redundant or unnecessary columns.
# 3. Explore the basic statistics of the dataset, including measures of central tendency and dispersion.
# 4. Perform data visualization to gain insights into the dataset. Generate appropriate plots, such as histograms, scatter plots, or bar plots, to visualize different aspects of the data.
# 5. Analyze the sales trends over time. Identify the busiest months and days of the week in terms of sales.
# 6. Explore the top-selling products and countries based on the quantity sold.
# 7. Identify any outliers or anomalies in the dataset and discuss their potential impact on the analysis.
# 8. Draw conclusions and summarize your findings from the exploratory data analysis.

# ## Task 1: Load the Data

# In[6]:


# your code here


# In[4]:


import pandas as pd
# Load dataset into a DataFrame
df = pd.read_excel('Online Retail.xlsx')

# Display first 5 rows
df.head()


# In[8]:


df.isnull().sum()


# In[9]:


df.dropna(subset=['Description','CustomerID'],inplace=True)


# In[10]:


df.isnull().sum()


# In[11]:


df.describe()


# In[23]:


import matplotlib.pyplot as plt


#histogram for Quantity
plt.figure(figsize=(10,5))
plt.hist(df['Quantity'],bins=10,color='orange',edgecolor='black')
plt.title('Distribution of Quantity')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

#histogram for UnitPrice
plt.figure(figsize=(10,5))
plt.hist(df['UnitPrice'],bins=10,color='Black',edgecolor='white')
plt.title('Distribution of Unit Price')
plt.xlabel('Unit Price')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# In[24]:


top_products = df.groupby('Description')['Quantity'].sum().nlargest(10)

plt.figure(figsize=(10,6))
top_products.plot(kind='barh', color='green')
plt.title('Top 10 Selling Products')
plt.xlabel('Quantity Sold')
plt.ylabel('Product')
plt.grid(axis='x')
plt.show()


# In[30]:


import pandas as pd
import matplotlib.pyplot as plt

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])


df['Month'] = df['InvoiceDate'].dt.month       
df['Date'] = df['InvoiceDate'].dt.date         
df['Year'] = df['InvoiceDate'].dt.year         
df['Hour'] = df['InvoiceDate'].dt.hour         

monthly_sales = df.groupby('Month')['Quantity'].sum()
daily_sales = df.groupby('Date')['Quantity'].sum()
yearly_sales = df.groupby('Year')['Quantity'].sum()
hourly_sales = df.groupby('Hour')['Quantity'].sum()

fig, axs = plt.subplots(2, 2, figsize=(16, 12))

#  Monthly Sales
axs[0, 0].bar(monthly_sales.index, monthly_sales.values, color='skyblue', edgecolor='black')
axs[0, 0].set_title('Total Sales by Month')
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Quantity Sold')
axs[0, 0].grid(True)

# Daily Sales
axs[0, 1].plot(daily_sales.index, daily_sales.values, color='darkorange')
axs[0, 1].set_title('Total Sales by Date')
axs[0, 1].set_xlabel('Date')
axs[0, 1].set_ylabel('Quantity Sold')
axs[0, 1].tick_params(axis='x', rotation=45)
axs[0, 1].grid(True)

# Yearly Sales
axs[1, 0].bar(yearly_sales.index, yearly_sales.values, color='lightgreen', edgecolor='black')
axs[1, 0].set_title('Total Sales by Year')
axs[1, 0].set_xlabel('Year')
axs[1, 0].set_ylabel('Quantity Sold')
axs[1, 0].grid(True)

# Hourly Sales
axs[1, 1].plot(hourly_sales.index, hourly_sales.values, marker='o', color='mediumpurple')
axs[1, 1].set_title('Total Sales by Hour of the Day')
axs[1, 1].set_xlabel('Hour (24h)')
axs[1, 1].set_ylabel('Quantity Sold')
axs[1, 1].grid(True)

# Step 7: Display the plots
plt.tight_layout()
plt.show()


# In[32]:


import matplotlib.pyplot as plt

# Get Top 5 Products
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(5)

# Get Top 5 Countries
top_countries = df.groupby('Country')['Quantity'].sum().sort_values(ascending=False).head(5)

# Setup figure with 2 subplots side-by-side
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# --- Plot 1: Top Products ---
axes[0].bar(top_products.index, top_products.values, color='teal', edgecolor='black')
axes[0].set_title('Top 5 Selling Products by Quantity')
axes[0].set_xlabel('Product Description')
axes[0].set_ylabel('Quantity Sold')
axes[0].tick_params(axis='x', rotation=45)
axes[0].grid(True)

# --- Plot 2: Top Countries ---
axes[1].bar(top_countries.index, top_countries.values, color='darkorange', edgecolor='black')
axes[1].set_title('Top 5 Countries by Quantity Sold')
axes[1].set_xlabel('Country')
axes[1].set_ylabel('Quantity Sold')
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(True)

# Final adjustments
plt.tight_layout()
plt.show()


# In[36]:


import seaborn as sns
import matplotlib.pyplot as plt

# Optional: Filter to make visualizations cleaner
filtered_df = df[(df['Quantity'] < 1000) & (df['UnitPrice'] < 100)]

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# --- 1. Boxen Plot: Quantity ---
sns.boxenplot(ax=axes[0, 0], x=filtered_df['Quantity'], color='skyblue')
axes[0, 0].set_title('Boxen Plot - Quantity Distribution')
axes[0, 0].set_xlabel('Quantity')
axes[0, 0].grid(True)

# --- 2. Boxen Plot: UnitPrice ---
sns.boxenplot(ax=axes[0, 1], x=filtered_df['UnitPrice'], color='orange')
axes[0, 1].set_title('Boxen Plot - Unit Price Distribution')
axes[0, 1].set_xlabel('Unit Price')
axes[0, 1].grid(True)

# --- 3. Scatter Plot: Quantity vs UnitPrice ---
sns.scatterplot(ax=axes[1, 0], data=filtered_df, x='UnitPrice', y='Quantity', alpha=0.5)
axes[1, 0].set_title('Scatter Plot - Quantity vs Unit Price')
axes[1, 0].set_xlabel('Unit Price')
axes[1, 0].set_ylabel('Quantity')
axes[1, 0].grid(True)

# --- 4. Violin Plot: Quantity ---
sns.violinplot(ax=axes[1, 1], x=filtered_df['Quantity'], inner='box', color='lightgreen')
axes[1, 1].set_title('Violin Plot - Quantity Distribution')
axes[1, 1].set_xlabel('Quantity')
axes[1, 1].grid(True)

# Layout adjustments
plt.tight_layout()
plt.show()


# ## Final Summary & Key Insights from Sales Analysis
# 
# After exploring the "Online Retail" dataset, several meaningful trends and patterns stood out that can drive better business decisions.
# 
# ---
# 
# ### Sales Patterns:
# - Sales volume was clearly seasonal — activity spiked in **November and December**, likely due to the holiday season.
# - Most purchases happened during **regular business hours (10 AM–3 PM)**, suggesting campaigns should be timed accordingly.
# - Weekdays generally saw higher sales compared to weekends, indicating more customer activity during the work week.
# 
# ---
# 
# ### Product & Country Insights:
# - The most frequently sold items were consistent, everyday products like:
#   - *WHITE HANGING HEART T-LIGHT HOLDER*
#   - *REGENCY CAKESTAND 3 TIER*
# - The **United Kingdom** accounted for the vast majority of sales, followed by countries like **Germany**, **France**, and **Netherlands** — all of which are key European markets.
# 
# ---
# 
# ### Outliers & Data Issues:
# - I found transactions with **negative quantities** — most likely returns or cancellations — which should be separated from forward-looking analysis.
# - Some rows had **extremely large quantities or unusually high prices**. These could be either bulk orders or data errors and should be flagged or filtered before doing any predictive modeling.
# 
# ---
# 
# ### Takeaways & Recommendations:
# - Focus inventory and marketing efforts leading into Q4 to align with seasonal demand.
# - Keep a close eye on returns and anomalies — they can distort trends if not accounted for.
# - Break down the data further by customer or region for more targeted insights.
# - Clean and validate transactional data regularly to improve decision-making and forecasting accuracy.
# 
# ---
# 
# ###  Final Note:
# This project helped me apply core data analysis techniques — from cleaning and visualization to trend detection and outlier handling — in a real-world business context. The insights gathered here can directly support sales planning, customer strategy, and operational improvements for any e-commerce business.
# 
