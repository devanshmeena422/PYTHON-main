import pandas as pd

df = pd.read_csv("sales.csv")

null_percent = (df.isnull().sum() / len(df)) * 100

print(null_percent)