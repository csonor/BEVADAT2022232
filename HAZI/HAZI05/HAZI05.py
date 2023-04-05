import numpy as np
import pandas as pd
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
import seaborn as sns


class KNNClassifier:
    def __init__(self, k: int, test_split_ratio: float) -> None:
        self.k = k
        self.test_split_ratio = test_split_ratio

    @property
    def k_neighbors(self) -> int:
        return self.k

    @staticmethod
    def load_csv(path: str) -> Tuple[pd.DataFrame, pd.Series]:
        dataset = pd.read_csv(path, header=None)
        dataset = dataset.sample(frac=1, random_state=42)
        x, y = dataset.iloc[:, :-1], dataset.iloc[:, -1]
        return x, y

    def train_test_split(self, features: pd.DataFrame, labels: pd.Series):
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"
        x_train, y_train = features.iloc[:train_size,
                                         :], labels.iloc[:train_size]
        x_test, y_test = features.iloc[train_size:,
                                       :], labels.iloc[train_size:]
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test

    def euclidean(self, element_of_x: pd.Series) -> pd.Series:
        return ((self.x_train - element_of_x)**2).sum(axis=1).apply(lambda x: x**0.5)

    def predict(self, x_test: pd.DataFrame):
        labels_pred = []
        for _, x_test_element in x_test.iterrows():
            distances = self.euclidean(x_test_element)
            distances = pd.DataFrame(sorted(zip(distances, self.y_train)))
            label_pred = distances.iloc[:self.k, 1].mode()
            labels_pred.append(label_pred)
        self.y_preds = pd.DataFrame(labels_pred).iloc[:, 0]

    def accuracy(self) -> float:
        true_positive = (self.y_test.reset_index(drop=True) ==
                         self.y_preds.reset_index(drop=True)).sum()
        return true_positive/len(self.y_test)*100

    def confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test, self.y_preds)
        return conf_matrix

    def best_k(self) -> Tuple[int, float]:
        orig_k = self.k
        best_k, best_accuracy = 0, 0.0
        for i in range(10):
            self.k = i+1
            self.predict(self.x_test)
            accuracy = self.accuracy()
            if accuracy > best_accuracy:
                best_k, best_accuracy = self.k, accuracy
        self.k = orig_k
        return best_k, round(best_accuracy, 2)
