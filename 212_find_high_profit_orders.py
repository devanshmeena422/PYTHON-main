import pandas as pd

df = pd.read_csv("sales.csv")

print(df[df["profit"] > 1000])