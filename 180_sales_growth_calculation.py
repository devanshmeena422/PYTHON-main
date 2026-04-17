import pandas as pd

df = pd.read_csv("sales.csv")

df["growth"] = df["sales"].pct_change()

print(df)