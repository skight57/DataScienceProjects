dataPrepX = dataPrep.drop(['selector', 'total_proteins'], axis='columns')
dataPrepY = dataPrep['selector']

cv_splits = StratifiedKFold(10, True, 123)
for train_index, test_index, in cv_splits.split(dataPrepX, dataPrepY):
    # create folds
    trainX = dataPrepX.iloc[train_index,]
    trainY = dataPrepY.iloc[train_index,]

    testX = dataPrepX.iloc[test_index,]
    testY = dataPrepY.iloc[test_index,]
    # print(trainY.value_counts())

    # model
    logisticModel = LogisticRegression(solver='lbfgs', max_iter=1200)
    logisticModel.fit(trainX, trainY)
    validation = logisticModel.predict(testX)

    # Evaluate
    # print(confusion_matrix(validation, testY))
    fold_accuracy = accuracy_score(validation, testY)
    # print(fold_accuracy)
    fold_precision = precision_score(validation, testY)
    fold_recall = recall_score(validation, testY)
    score = score.append({'Accuracy': fold_accuracy, 'Precision': fold_precision, 'Recall': fold_recall},
                         ignore_index=True)

logit_score = logit_score.append(
    {'Model': 'No Total Proteins', 'Accuracy': score.Accuracy.mean(), 'Precision': score.Precision.mean(),
     'Recall': score.Recall.mean()}, ignore_index=True)
logit_score
