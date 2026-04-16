import pandas as pd

df = pd.read_csv("data.csv")

bottom5 = df["value"].nsmallest(5)

print(bottom5)