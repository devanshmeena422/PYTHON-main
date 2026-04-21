import pandas as pd

df = pd.read_csv("sales.csv")

print(df["customer"].value_counts().idxmax())