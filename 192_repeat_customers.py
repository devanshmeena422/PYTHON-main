import pandas as pd

df = pd.read_csv("sales.csv")

counts = df["customer"].value_counts()

print(counts[counts > 1])