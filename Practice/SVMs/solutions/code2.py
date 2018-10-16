def split_data(X, y, start, end):
    X_train = np.concatenate((X[:start], X[end:]), axis=0)
    y_train = np.concatenate((y[:start], y[end:]), axis=0)
    X_test  = X[start:end]
    y_test  = y[start:end]
    return X_train, y_train, X_test, y_test

C = [0.001, 0.01, 0.1, 1.0, 10, 42, 100, 1000] # Tested values of C
k = 10 # k-fold CV: number of subsets
n = int(len(X)/k) # length subsets

global_acc = []

for c in C:
    accuracies = []
    for i in range(k):
        X_train, y_train, X_test, y_test = split_data(X, y, i*n, (i+1)*n)
        mySVC = svm.SVC(kernel='linear', C=c)
        mySVC.fit(X_train, y_train)
        y_pred = mySVC.predict(X_test)
        n_error = sum(list(int(not y_pred[i] == y_test[i]) for i in range(len(y_test))))
        error_rate = n_error / n # error rate
        accuracy = 1 - error_rate # accuracy
        accuracies.append(accuracy)
    global_acc.append( [np.mean(accuracies), c])
    
for acc, c in global_acc:
    print(c, "\t --> \t", acc)
