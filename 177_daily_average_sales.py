import pandas as pd

df = pd.read_csv("sales.csv")

result = df.groupby("date")["sales"].mean()

print(result)