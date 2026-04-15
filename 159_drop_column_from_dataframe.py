import pandas as pd

df = pd.read_csv("data.csv")

df = df.drop("column_name", axis=1)

print(df)