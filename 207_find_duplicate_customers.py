import pandas as pd

df = pd.read_csv("sales.csv")

duplicates = df[df["customer"].duplicated()]

print(duplicates)