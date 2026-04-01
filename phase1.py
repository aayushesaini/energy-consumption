import pandas as pd

df = pd.read_excel("energy.xlsx")
n = df.isnull().sum()

if n<=50:
    df = df.dropna()
else:
    df.fillna(df.mode().iloc[0], inplace=True)
data = data.drop_duplicates()

print(df.describe())

import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data['energy'])
Q1 = data['energy'].quantile(0.25)
Q3 = data['energy'].quantile(0.75)
IQR = Q3 - Q1
data = data[(data['energy'] >= Q1 - 1.5*IQR) & (data['energy'] <= Q3 + 1.5*IQR)]

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

df.hist(figsize=(12,8))
plt.show()

plt.plot(df['time'], df['energy'], '.')
plt.xlabel("Time")
plt.ylabel("Energy")
plt.show()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data[['temperature','students']] = scaler.fit_transform(data[['temperature','students']])
plt.scatter(df['students'], df['energy'])
plt.xlabel("Students")
plt.ylabel("Energy")
plt.show()

