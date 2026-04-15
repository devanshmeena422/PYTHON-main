import pandas as pd

df = pd.read_csv("data.csv")

counts = df["category"].value_counts()

print(counts)