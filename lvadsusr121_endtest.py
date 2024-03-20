# -*- coding: utf-8 -*-
"""LVADSUSR121-ENDTEST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EKROwGhj7t_GpQvLbaRHGX4oIYONiPqD
"""

#1
import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/Pandas Practice/Walmart_Dataset Python_Final_Assessment.csv')
print(df)
print("Data types of columns:")
print(df.dtypes)
print()
print("summary:")
print(df.describe())
print()
print()

#2
no_of_duplicates = df.duplicated().sum()
print(no_of_duplicates)
df.drop_duplicates(inplace=True)
df['Sales'].fillna(0,inplace=True)
missing_values = df.isnull().sum()
print("Missing values:")
print(missing_values)
print()
data = df.dropna()
duplicate_entries = data.duplicated().sum()
print("Number of duplicate entries:", duplicate_entries)
print()
data = data.drop_duplicates()

#3
import numpy as np
df1 = df.groupby('Category')['Sales'].aggregate('mean')
print("Average of sales",df1)
df2 = np.std(df['Sales'])
print("standard deviation : ",df2)
df3 = np.var(df['Sales'])
print("Variance : ",df3)
print("Data types of columns:")



numerical_data = df.select_dtypes(include=['int64', 'float64'])

mode_values = numerical_data.mode()
mean_values = numerical_data.mean()
data_range = numerical_data.max() - numerical_data.min()
variance = numerical_data.var()
std_deviation = numerical_data.std()

#4
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('Plotting for Distribution of sales')
plt.figure(figsize=(4, 4))
sns.histplot(df['Sales'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

print('Sales vs profit')
plt.figure(figsize=(4, 4))
sns.scatterplot(data=df, x='Sales', y='Profit', color='green')
plt.title('Sales vs. Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()

#5
print(df.corr())

#6
import sclt as stat
Z score = stat.df['Sales']
outliers = abs(z score) > 12
print(outliers)

#7
# Trends analysis:
# 1.analyze the scales and profit trends over the year. Are there any noticeable patterns or seasonal variations?
df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Year'] = df['Order Date'].dt.year

yearly_data = df.groupby('Year').agg({
    'Sales': 'sum',
    'Profit': 'sum'}).reset_index()

plt.figure(figsize=(6, 6))
plt.plot(yearly_data['Year'], yearly_data['Sales'], marker='o', label='Total Sales', color='blue')
plt.plot(yearly_data['Year'], yearly_data['Profit'], marker='o', label='Total Profit', color='green')
plt.title('Sales and Profit Trends Over the Years')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.xticks(yearly_data['Year'])
plt.legend()
plt.show()

#2.Product category that has shown the most growth in terms of sales over the years
category_sales = df.groupby(['Year', 'Category'])['Sales'].sum().unstack()

plt.figure(figsize=(12, 8))
category_sales.plot(kind='line', marker='o')
plt.title('Sales Trend for Each Product Category Over the Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.xticks(yearly_data['Year'])
plt.legend(title='Category')
plt.show()

#2 customer analysis
customer_group = df.groupby('EmailID')


orders_per_customer = customer_group.size()
total_sales_per_customer = customer_group['Sales'].sum()

customer_stats = pd.DataFrame({
    'Number of Orders': orders_per_customer,
    'Total Sales': total_sales_per_customer
})

sorted_customers = customer_stats.sort_values(by=['Number of Orders', 'Total Sales'], ascending=False)

top_5_customers = sorted_customers.head(5)

print("Top 5 Customers:")
print(top_5_customers)

"""Comprehensive Analytics
i) The supply chain can be increased by increasing the quality of the products and complete faultless order delivery.The product should be of good quality to increase sales velocity.Send regular customers frequent offers.

ii) The geographic distribution sales can be increased by selling the products which is more required in that area.The sales can also increased by good quality natural products

iii) It can be increased by promoting like advertisements, real time situations connection products etc.
"""