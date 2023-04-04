import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.DecisionTreeClassifier import DecisionTreeClassifier

data = pd.read_csv("D:/Temp/progammin/egyetem/W6H9QV_BEVADAT2022232/HAZI/HAZI06/NJ_60k.csv")

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1, 1)
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=.2, random_state=41)

classifier = DecisionTreeClassifier(3, 3)
classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)
print(accuracy_score(Y_test, Y_pred))
