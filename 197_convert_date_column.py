import pandas as pd

df = pd.read_csv("sales.csv")

df["date"] = pd.to_datetime(df["date"])

print(df.dtypes)