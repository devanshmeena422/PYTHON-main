import pandas as pd

df = pd.read_csv("data.csv")

df["ratio"] = df["value1"] / df["value2"]

print(df)