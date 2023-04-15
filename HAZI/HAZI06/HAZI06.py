import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.DecisionTreeClassifier import DecisionTreeClassifier

data = pd.read_csv("HAZI/HAZI06/NJ_60k.csv")

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1, 1)
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=.2, random_state=41)

classifier = DecisionTreeClassifier(90, 11)
classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)
print(accuracy_score(Y_test, Y_pred))


#min_samples_split=3, max_depth=3 -> 0.7839166666666667
#min_samples_split=5, max_depth=5 -> 0.7885833333333333
#min_samples_split=15, max_depth=5 -> 0.7885833333333333
#min_samples_split=30, max_depth=10 -> 0.80075
#min_samples_split=45, max_depth=13 -> 0.7980833333333334
#min_samples_split=60, max_depth=12 -> 0.8016666666666666
#min_samples_split=80, max_depth=15 -> 0.797
#min_samples_split=85, max_depth=10 -> 0.8014166666666667
#min_samples_split=90, max_depth=12 -> 0.80175
#############################################
#min_samples_split=90, max_depth=11 -> 0.803# best
#############################################
#min_samples_split=90, max_depth=10 -> 0.8018333333333333
#min_samples_split=110, max_depth=11 -> 0.80275
#min_samples_split=120, max_depth=12 -> 0.80125
