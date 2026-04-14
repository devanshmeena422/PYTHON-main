import pandas as pd

df = pd.read_csv("data.csv")

correlation = df.corr()

print(correlation)