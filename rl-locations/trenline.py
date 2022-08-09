import numpy as np
import pandas as pd


data_counts_two_of_ones = pd.read_csv("./data3/data_counts_two_of_ones.csv")


def trendline(x, y, order=1):
    return np.polyfit(x, y, order)[-2]


data_counts_two_of_ones.groupby('cid').apply(
    lambda subdf: trendline(subdf['month'].values, subdf['spending'].values)
)
