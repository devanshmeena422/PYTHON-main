import pandas as pd

df = pd.read_csv("data.csv")

result = df.groupby("category")["value"].sum()

print(result)