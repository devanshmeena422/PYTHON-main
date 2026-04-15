import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

plt.plot(df["value"])
plt.title("CSV Data Plot")

plt.show()