# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'Date': pd.date_range(start='2022-01-01', periods=10),
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C', 'A'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing', 'Home', 'Electronics', 'Clothing', 'Home', 'Electronics'],
    'Sales': [150, 200, 120, 80, 250, 90, 180, 210, 110, 160],
    'Expenses': [80, 50, 60, 30, 70, 40, 50, 90, 30, 60],
    'Profit': [70, 150, 60, 50, 180, 50, 130, 120, 80, 100]
}

df = pd.DataFrame(data)

# Display the dataset
print("Sample Data:")
print(df)

# Basic statistics of the dataset
print("\nBasic Statistics:")
print(df.describe())

# Data visualization - Sales over time
plt.figure(figsize=(10, 6))
for product in df['Product'].unique():
    product_data = df[df['Product'] == product]
    plt.plot(product_data['Date'], product_data['Sales'], label=f'Product {product}')

plt.title('Sales Over Time by Product')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()
