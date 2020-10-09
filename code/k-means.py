import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import mglearn
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

X = pd.read_csv('../data/out/task1_3_2.csv', encoding='gbk')
X = X[['消费总额', '常去消费地点']]

scaler = MinMaxScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)
print(X)
print(X_scaled)

kmeans = KMeans(n_clusters=3)
kmeans.fit(X_scaled)
print("Cluster memberships:\n{}".format(kmeans.labels_))
print(kmeans.cluster_centers_)
mglearn.discrete_scatter(X_scaled[:, 0], X_scaled[:, 1], kmeans.labels_, markers='o')
mglearn.discrete_scatter(
    kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], [0, 1, 2],
    markers='^', markeredgewidth=2)
plt.show()
