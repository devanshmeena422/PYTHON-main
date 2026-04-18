import pandas as pd

df = pd.read_csv("sales.csv")

print(df.groupby("category")["sales"].mean())