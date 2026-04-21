import pandas as pd

df = pd.read_csv("sales.csv")

df = df.dropna()

df.to_csv("cleaned_sales.csv", index=False)

print("File saved successfully")