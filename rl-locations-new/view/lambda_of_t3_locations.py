import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv("data1/data_locations_of_ones.csv")
df = df.head(10_000)
df.plot(x='count', y='loc', kind='scatter', c="count", colormap='plasma')
plt.savefig("lambda_locations_from_data1_ones.png")

df = pd.read_csv("data1/data_locations_of_zeros.csv")
df = df.head(10_000)
df.plot(x='count', y='loc', kind='scatter', c="count", colormap='plasma')
plt.savefig("lambda_locations_from_data1_zeros.png")
