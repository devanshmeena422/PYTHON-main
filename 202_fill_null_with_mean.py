import pandas as pd

df = pd.read_csv("sales.csv")

df["sales"] = df["sales"].fillna(df["sales"].mean())

print(df)