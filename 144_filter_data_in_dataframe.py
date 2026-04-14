import pandas as pd

df = pd.read_csv("data.csv")

filtered = df[df["value"] > 50]

print(filtered)