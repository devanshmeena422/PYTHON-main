import pandas as pd

df = pd.read_csv("data.csv")

unique_count = df["category"].nunique()

print("Unique values:", unique_count)