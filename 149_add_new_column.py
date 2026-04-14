import pandas as pd

df = pd.read_csv("data.csv")

df["double_value"] = df["value"] * 2

print(df)