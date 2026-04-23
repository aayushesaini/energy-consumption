from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

features = ['temperature', 'students']

data[features] = scaler.fit_transform(data[features])
