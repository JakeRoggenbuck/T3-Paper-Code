import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("data1/data_locations_of_ones.csv")

plt.figure()
plt.xlim(min(df.count), max(df.count))
ax = sns.regplot('count', 'loc_in_t', data=df)
plt.show()

# df.plot(x='count', y='loc_in_t', kind='scatter', c="count", colormap='plasma')
# df.plot(df["count"], a*df["count"]+b)
# plt.show()
# plt.savefig("lambda_locations_from_data1_ones.png")

# df = pd.read_csv("data1/data_locations_of_zeros.csv")
# df.plot(x='count', y='loc_in_t', kind='scatter', c="count", colormap='plasma')
# plt.savefig("lambda_locations_from_data1_zeros.png")
