import pandas as pd

df = pd.read_csv("sales.csv")

print("Total Sales:", df["sales"].sum())
print("Average Sales:", df["sales"].mean())
print("Max Sales:", df["sales"].max())