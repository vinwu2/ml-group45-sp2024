import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


file_path = "/Users/rohanaluri/Desktop/datapreprocessed.csv" 
nba_data = pd.read_csv(file_path)

numeric_nba_data = nba_data.select_dtypes(include=[np.number])

corr = numeric_nba_data.corr()

fig, ax = plt.subplots(figsize=(12, 10))

cax = ax.imshow(corr, interpolation='nearest', cmap='coolwarm')
fig.colorbar(cax)

ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=90)
ax.set_yticklabels(corr.columns)

plt.title('Heatmap of NBA Feature Correlations', pad=20)

plt.show()