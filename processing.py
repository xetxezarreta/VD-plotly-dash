import numpy as np
import pandas as pd
import utils
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score

df = pd.read_csv('data/diabetes.csv')
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0, stratify=y)

def get_indicators(algorithm):
    algorithm = utils.algorithms[algorithm]
    model = algorithm.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    f1score = f1_score(y_test, y_pred)
    rocauc = roc_auc_score(y_test, y_pred)

    return accuracy, f1score, rocauc
