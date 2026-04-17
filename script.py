import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("Shape:", df.shape)
print("Columns:", df.columns)
print("Missing values:\n", df.isnull().sum())

df["Total Sales"] = df["Units Sold"] * df["Unit Price"]

sales_by_product = df.groupby("Product")["Total Sales"].sum().sort_values(ascending=False)
print("\nSales by Product:\n", sales_by_product)

plt.figure()
sales_by_product.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("total_sales_by_product.png")
plt.show()

sales_by_region = df.groupby("Region")["Total Sales"].sum().sort_values(ascending=False)
print("\nSales by Region:\n", sales_by_region)

plt.figure()
sales_by_region.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("total_sales_by_region.png")
plt.show()

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_sales = df.groupby("Month")["Total Sales"].sum()
print("\nMonthly Sales:\n", monthly_sales)

plt.figure()
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()

sales_by_category = df.groupby("Category")["Total Sales"].sum().sort_values(ascending=False)
print("\nSales by Category:\n", sales_by_category)

print("\n=== FINAL INSIGHTS ===")
print("Top Product:", sales_by_product.idxmax())
print("Top Region:", sales_by_region.idxmax())
print("Top Category:", sales_by_category.idxmax())
print("Total Sales:", df["Total Sales"].sum())