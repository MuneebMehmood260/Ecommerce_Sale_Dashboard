import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel(r"Dataset\ecommerce_sales_data.xlsx")

# print(df.head())
# print(df.info())
# print(df.isnull().sum())
# print(df.describe())

print(df.duplicated().sum())

# detect outliers using IQR method
q1 = df["Sales"].quantile(0.25)
q3 = df["Sales"].quantile(0.75)
IQR = q3 - q1
lower_bound = q1-1.5*IQR
upper_bound = q3+1.5*IQR
outliers = df[(df["Sales"] < lower_bound) | (df["Sales"] > upper_bound)]
# print(outliers)

plt.boxplot(df["Sales"])
plt.title("Boxplot of Sales")
# plt.show()
df.to_excel(r"Dataset\ecommerce_sales_data.xlsx" , index=False)