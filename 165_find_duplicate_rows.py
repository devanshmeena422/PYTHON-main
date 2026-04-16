import pandas as pd

df = pd.read_csv("data.csv")

duplicates = df[df.duplicated()]

print(duplicates)