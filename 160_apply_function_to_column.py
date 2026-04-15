import pandas as pd

df = pd.read_csv("data.csv")

df["value_squared"] = df["value"].apply(lambda x: x**2)

print(df)