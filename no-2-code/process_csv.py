import pandas as pd

df = pd.read_csv("./out.csv")

df = df['num'].value_counts().reset_index()
df.columns = ['num', 'count']

print(df)
