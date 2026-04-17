import pandas as pd

df = pd.read_csv("sales.csv")

result = df.groupby("month")["sales"].sum()

print(result)