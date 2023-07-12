'''
    analytical program for analyzing sales data of a company
'''
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
import seaborn as sns
import matplotlib.pyplot as plt

# 1. collect data
sales_data = pd.read_csv('sales_data.csv')

# 2. data loading
print(sales_data.head())

# 3. clearing data
sales_data.dropna(inplace=True)
# sales volume for each product
sales_by_product = sales_data.groupby('product')['sales'].sum()

# sales volume for each month
sales_by_month = sales_data.groupby('month')['sales'].sum()

# Average and standard deviation of sales for each product
sales_mean_by_product = sales_data.groupby('product')['sales'].mean()
sales_std_by_product = sales_data.groupby('product')['sales'].std()

# comparison of average sales between two products by ttest
product_A_sales = sales_data[sales_data['product'] == 'A']['sales']
product_B_sales = sales_data[sales_data['product'] == 'B']['sales']
t_stat, p_value = ttest_ind(product_A_sales, product_B_sales)

# 5. data analysis
# Bar chart of sales for each product
plt.bar(sales_by_product.index, sales_by_product.values)
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.show()

# line chart of sales for each month
plt.plot(sales_by_month.index, sales_by_month.values)
plt.title('Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

# violin chart of mean and standard devision of sales for each product
sns.violinplot(x=sales_data['product'], y=sales_data['sales'])
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.show()

# 6. display data
# 10 the first row of data
print(sales_data.head(10))

# 7. data storage
#the cleared data is stored in the csv file
sales_data.to_csv('cleaned_sales_data.csv')