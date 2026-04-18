import pandas as pd

df = pd.read_csv("sales.csv")

city_sales = df.groupby("city")["sales"].sum()

print(city_sales.idxmin())