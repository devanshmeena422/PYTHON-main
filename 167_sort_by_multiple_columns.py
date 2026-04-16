import pandas as pd

df = pd.read_csv("data.csv")

sorted_df = df.sort_values(by=["category", "value"])

print(sorted_df)