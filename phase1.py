import pandas as pd

df = pd.read_excel("energy.xlsx")
n = df.isnull().sum()

if n<=50:
    df = df.dropna()
else:
    df.fillna(df.mode().iloc[0], inplace=True)

print(df.describe())

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

df.hist(figsize=(12,8))
plt.show()

plt.plot(df['time'], df['energy'], '.')
plt.xlabel("Time")
plt.ylabel("Energy")
plt.show()

plt.scatter(df['students'], df['energy'])
plt.xlabel("Students")
plt.ylabel("Energy")
plt.show()

