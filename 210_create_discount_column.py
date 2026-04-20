import pandas as pd

df = pd.read_csv("sales.csv")

df["discount"] = df["sales"] * 0.10

print(df)