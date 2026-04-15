import pandas as pd

df = pd.read_csv("data.csv")

df = df.rename(columns={"old_name": "new_name"})

print(df)
