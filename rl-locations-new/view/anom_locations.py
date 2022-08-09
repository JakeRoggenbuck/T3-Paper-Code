import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv("data2/data_locations_of_anomalies.csv")


def normal_scale():
    df.plot(x='anom_percent', y='loc_in_t', kind='scatter', c="anom_percent", colormap='plasma')

    plt.savefig("lambda_anom_percent.png")


def log_scale():
    df.plot(x='anom_percent', y='loc_in_t', kind='scatter', c="anom_percent", colormap='plasma')
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig("lambda_anom_percent_log.png")

normal_scale()
log_scale()
