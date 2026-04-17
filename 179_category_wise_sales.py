import pandas as pd

df = pd.read_csv("sales.csv")

result = df.groupby("category")["sales"].sum()

print(result)