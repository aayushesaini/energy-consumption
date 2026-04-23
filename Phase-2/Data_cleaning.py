import pandas as pd

df = pd.read_excel("energy.xlsx")

data = data.drop_duplicates()

n = df.isnull().sum()

if n<=50:
    df = df.dropna()
else:
    df.fillna(df.mode().iloc[0], inplace=True)
