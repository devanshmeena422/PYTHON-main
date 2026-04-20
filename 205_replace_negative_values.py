import pandas as pd

df = pd.read_csv("sales.csv")

df["sales"] = df["sales"].apply(lambda x: 0 if x < 0 else x)

print(df)