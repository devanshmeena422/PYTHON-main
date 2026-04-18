import pandas as pd

df = pd.read_csv("sales.csv")

result = df.groupby("product")["sales"].sum().nlargest(5)

print(result)