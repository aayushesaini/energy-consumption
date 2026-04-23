import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data['energy'])

Q1 = data['energy'].quantile(0.25)
Q3 = data['energy'].quantile(0.75)

IQR = Q3 - Q1

data = data[(data['energy'] >= Q1 - 1.5*IQR) & (data['energy'] <= Q3 + 1.5*IQR)]
