import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv("data2/data_locations_of_anomalies.csv")
df.plot(x='anom_percent', y='loc_in_t', kind='scatter', c="anom_percent", colormap='plasma')
plt.xscale('log')
plt.yscale('log')
plt.savefig("lambda_anom_percent.png")
