import pandas as pd

df = pd.read_csv("sales.csv")

df = df.dropna()

print(df)