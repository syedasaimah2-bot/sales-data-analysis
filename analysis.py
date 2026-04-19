import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sales.csv")

print("\n--- Sales Data ---")
print(df)

df["Total"] = df["Price"] * df["Quantity"]

print("\n--- Data with Total Revenue ---")
print(df)

total_sales = df["Total"].sum()
print("\nTotal Revenue:", total_sales)

best_product = df.groupby("Product")["Total"].sum().sort_values(ascending=False)

print("\n--- Best Selling Products ---")
print(best_product)
# Sales by Product
product_sales = df.groupby("Product")["Total"].sum()

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.show()