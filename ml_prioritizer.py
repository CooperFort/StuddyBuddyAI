from sklearn.tree import DecisionTreeClassifier
import numpy as np

class TaskPrioritizer:
    def __init__(self):
        self.training_data = np.array([
            [1, 5, 1], [2, 4, 2], [3, 3, 3], [7, 2, 4], [14, 1, 5]
        ])
        self.model = DecisionTreeClassifier()
        self.train_model()

    def train_model(self):
        X = self.training_data[:, :2]
        y = self.training_data[:, 2]
        self.model.fit(X, y)

    def predict_priority(self, days_to_deadline, importance):
        return self.model.predict([[days_to_deadline, importance]])[0]
