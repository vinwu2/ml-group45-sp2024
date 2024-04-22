import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
forest = pd.read_csv("C:/Users/rohit/Downloads/datapreprocessed.csv")
forest = forest.drop(['game_id', 'date'], axis = 1)
forest.dropna(inplace=True)
forest = pd.get_dummies(forest)
labels = np.array(forest['hit_over'])
forest = forest.drop('hit_over', axis = 1)
forest_list = list(forest.columns)
forest = np.array(forest)

train_features, test_features, train_labels, test_labels = train_test_split(forest, labels, test_size = 0.25, random_state=42)

rf = RandomForestClassifier(n_estimators = 1000, random_state = 35)
rf.fit(train_features, train_labels)
predictions = rf.predict(test_features)
errors = abs(predictions - test_labels)

accuracy = accuracy_score(test_labels, predictions)
print(accuracy*100)