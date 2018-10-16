from sklearn.preprocessing import StandardScaler

X = data.iloc[:,1:23]  # all rows, all the features and no labels
y = data.iloc[:, 0]  # all rows, label only

scaler = StandardScaler()
X = scaler.fit_transform(X)
print(X[:3,:])
