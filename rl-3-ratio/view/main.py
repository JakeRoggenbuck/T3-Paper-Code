import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv("data/data_locations_of_ones.csv")
df = df.head(10000)

df.plot(x='loc_in_t', y='count', kind='scatter', c="count", colormap='plasma')
plt.savefig("lambda_ratio_from_data1_ones_10000.png")
