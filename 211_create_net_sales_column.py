import pandas as pd

df = pd.read_csv("sales.csv")

df["net_sales"] = df["sales"] - (df["sales"] * 0.10)

print(df)