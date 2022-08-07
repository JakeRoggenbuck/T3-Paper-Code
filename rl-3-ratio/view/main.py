import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv("data/data_locations_of_ones.csv")
df = df.head(100)

df.plot(x='loc_in_t', y='count', kind='scatter', c="#58d68d", colormap='plasma')
plt.xlabel("Location in T")
plt.ylabel("Ratio of threes / none threes")
plt.savefig("lambda_ratio_from_data1_ones_100.png")


df = pd.read_csv("data/data_locations_of_ones.csv")
df = df.head(10000)

df.plot(x='loc_in_t', y='count', kind='scatter', c="#58d68d", colormap='plasma')
plt.xlabel("Location in T")
plt.ylabel("Ratio of threes / none threes")
plt.savefig("lambda_ratio_from_data1_ones_10000.png")

df = pd.read_csv("data/data_locations_of_zeros.csv")
df = df.head(100)

df.plot(x='loc_in_t', y='count', kind='scatter', c="#58d68d", colormap='plasma')
plt.xlabel("Location in T")
plt.ylabel("Ratio of threes / none threes")
plt.savefig("lambda_ratio_from_data1_zeros_100.png")

df = pd.read_csv("data/data_locations_of_zeros.csv")
df = df.head(10000)

df.plot(x='loc_in_t', y='count', kind='scatter', c="#58d68d", colormap='plasma')
plt.xlabel("Location in T")
plt.ylabel("Ratio of threes / none threes")
plt.savefig("lambda_ratio_from_data1_zeros_10000.png")
