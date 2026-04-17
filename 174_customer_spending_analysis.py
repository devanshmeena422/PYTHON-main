import pandas as pd

df = pd.read_csv("sales.csv")

result = df.groupby("customer")["sales"].sum()

print(result)