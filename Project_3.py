import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df = pd.read_csv('sales_data.csv')

# Display the first few rows of the dataset
df.head()
# Check for missing values
df.isnull().sum()
# Dropping rows with missing values
df.dropna(inplace=True)

# Or, fill missing values with the mean or a placeholder
df['order_amount'].fillna(df['order_amount'].mean(), inplace=True)
# Dropping rows with missing values
df.dropna(inplace=True)
# Convert 'order_date' to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Check data types
df.dtypes
# Remove duplicate rows
df.drop_duplicates(inplace=True)
# Summary statistics
df.describe()

# Plot the distribution of order amounts
plt.figure(figsize=(10, 6))
sns.histplot(df['order_amount'], kde=True, color='skyblue', bins=30)
plt.title('Distribution of Order Amount')
plt.xlabel('Order Amount')
plt.ylabel('Frequency')
plt.show()

# Sales by region
sales_by_region = df.groupby('region')['order_amount'].sum().sort_values(ascending=False)

# Plot sales by region
plt.figure(figsize=(12, 6))
sales_by_region.plot(kind='bar', color='coral')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.show()


# Sales trends over time
df['year_month'] = df['order_date'].dt.to_period('M')
sales_trends = df.groupby('year_month')['order_amount'].sum()

# Plot sales trends
plt.figure(figsize=(12, 6))
sales_trends.plot(kind='line', color='green')
plt.title('Sales Trends Over Time')
plt.xlabel('Month')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.show()

# Calculate average order value
aov = df['order_amount'].mean()
print(f'Average Order Value: {aov}')


# Sales by product
sales_by_product = df.groupby('product_id')['order_amount'].sum().sort_values(ascending=False).head(10)

# Plot top 10 products
plt.figure(figsize=(12, 6))
sales_by_product.plot(kind='bar', color='royalblue')
plt.title('Top 10 Best-Selling Products')
plt.xlabel('Product ID')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.show()


# Payment method breakdown
payment_method_sales = df.groupby('payment_method')['order_amount'].sum().sort_values(ascending=False)

# Plot payment method breakdown
plt.figure(figsize=(8, 6))
payment_method_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightyellow'])
plt.title('Sales Breakdown by Payment Method')
plt.ylabel('')  # Hide the y-label
plt.show()


# Correlation heatmap
corr_matrix = df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()


print("Key Insights:")
print(f"1. The top region in terms of sales is {sales_by_region.idxmax()} with a total sales of {sales_by_region.max()}.")
print(f"2. The average order value (AOV) is {aov:.2f}.")
print(f"3. The month with the highest sales is {sales_trends.idxmax()} with a total sales amount of {sales_trends.max():,.2f}.")
print(f"4. The most popular payment method is {payment_method_sales.idxmax()}, which accounts for {payment_method_sales.max():.1f}% of total sales.")


# Save the cleaned dataset to a new CSV file
df.to_csv('cleaned_sales_data.csv', index=False)
