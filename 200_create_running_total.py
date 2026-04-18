import pandas as pd

df = pd.read_csv("sales.csv")

df["running_total"] = df["sales"].cumsum()

print(df)