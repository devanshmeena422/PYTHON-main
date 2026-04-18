import pandas as pd

df = pd.read_csv("sales.csv")

avg = df["sales"].mean()

print(df[df["sales"] > avg])