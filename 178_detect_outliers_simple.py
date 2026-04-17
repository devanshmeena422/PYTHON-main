import pandas as pd

df = pd.read_csv("sales.csv")

avg = df["sales"].mean()

outliers = df[df["sales"] > 2 * avg]

print(outliers)