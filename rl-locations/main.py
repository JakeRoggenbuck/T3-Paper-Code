import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("./data/data_counts_two_of_zeros.csv")

df.plot(x='x', y='y', kind='scatter', c="type", colormap='plasma')

plt.show()
