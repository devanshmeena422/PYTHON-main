import pandas as pd

df = pd.read_csv("data.csv")

null_counts = df.isnull().sum()

print(null_counts)