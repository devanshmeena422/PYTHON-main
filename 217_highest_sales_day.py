import pandas as pd

df = pd.read_csv("sales.csv")

row = df.loc[df["sales"].idxmax()]

print(row["date"])