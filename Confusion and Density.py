import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

forest = pd.read_csv("/Users/rohanaluri/Desktop/datapreprocessed.csv")
forest = forest.drop(['game_id', 'date'], axis=1)
forest.dropna(inplace=True)
forest = pd.get_dummies(forest)
labels = np.array(forest['hit_over'])
forest = forest.drop('hit_over', axis=1)
forest_list = list(forest.columns)
forest = np.array(forest)

train_features, test_features, train_labels, test_labels = train_test_split(forest, labels, test_size=0.25, random_state=42)

rf = RandomForestClassifier(n_estimators=1000, random_state=35)
rf.fit(train_features, train_labels)
predictions = rf.predict(test_features)

accuracy = accuracy_score(test_labels, predictions)
print(f"Accuracy: {accuracy*100:.2f}%")

cm = confusion_matrix(test_labels, predictions)

fig, ax = plt.subplots(figsize=(8, 8))
cax = ax.matshow(cm, cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
fig.colorbar(cax)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.xticks([0, 1], ['0', '1'])
plt.yticks([0, 1], ['0', '1'])

for (i, j), value in np.ndenumerate(cm):
    plt.text(j, i, f'{value}', ha='center', va='center', color='black')

plt.show()


probabilities = rf.predict_proba(test_features)[:, 1]

plt.figure(figsize=(10, 6))
plt.hist(probabilities, bins=50, density=True, alpha=0.6, color='b')
plt.title('Density Plot of Predicted Probabilities for the Positive Class')
plt.xlabel('Probability')
plt.ylabel('Density')

from scipy.stats import gaussian_kde
density = gaussian_kde(probabilities)
xs = np.linspace(0, 1, 200)
plt.plot(xs, density(xs), 'r-')
plt.show()