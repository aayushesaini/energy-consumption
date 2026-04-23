plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

corr_matrix = df.corr()
print(corr_matrix)
