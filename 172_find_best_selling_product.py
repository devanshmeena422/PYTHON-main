import pandas as pd

df = pd.read_csv("sales.csv")

result = df.groupby("product")["sales"].sum()

best_product = result.idxmax()

print("Best selling product:", best_product)