import pandas as pd

df = pd.read_csv("sales.csv")

high_value = df[df["sales"] > 1000]

print(high_value)