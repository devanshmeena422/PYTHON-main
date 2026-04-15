import pandas as pd

df = pd.read_csv("data.csv")

top5 = df["value"].nlargest(5)

print(top5)