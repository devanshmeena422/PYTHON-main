import pandas as pd

df = pd.read_csv("sales.csv")

result = df.groupby("product")["profit"].mean()

print(result)