import pandas as pd
from matplotlib import pyplot as plt

data_counts_two_of_zeros = pd.read_csv("./data/data_counts_two_of_zeros.csv")
data_counts_two_of_zeros.plot(x='x', y='y', kind='scatter', c="type", colormap='plasma')
plt.savefig("data_counts_two_of_zeros.png")

data_counts_two_of_ones = pd.read_csv("./data/data_counts_two_of_ones.csv")
data_counts_two_of_ones.plot(x='x', y='y', kind='scatter', c="type", colormap='plasma')
plt.savefig("data_counts_two_of_ones.png")

data_counts_two_of_zeros = pd.read_csv("./data2/data_counts_two_of_zeros.csv")
data_counts_two_of_zeros.plot(x='x', y='y', kind='scatter', c="type", colormap='plasma')
plt.savefig("data_counts_two_of_zeros_two.png")

data_counts_two_of_ones = pd.read_csv("./data2/data_counts_two_of_ones.csv")
data_counts_two_of_ones.plot(x='x', y='y', kind='scatter', c="type", colormap='plasma')
plt.savefig("data_counts_two_of_ones_two.png")
