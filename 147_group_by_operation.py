import pandas as pd

df = pd.read_csv("data.csv")

grouped = df.groupby("category")["value"].sum()

print(grouped)