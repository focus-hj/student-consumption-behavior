import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

X = pd.read_csv('../data/out/task1_3_2.csv', encoding='gbk')
X = X[['性别', '超市消费总额', '食堂消费总额', '当月用卡总次数', '常去消费地点']]

X_man = X[X['性别'] == 0].drop('性别', axis=1)
X_woman = X[X['性别'] == 1].drop('性别', axis=1)

scaler = MinMaxScaler()
scaler.fit(X_man)
X_man_scaled = scaler.transform(X_man)
scaler.fit(X_woman)
X_woman_scaled = scaler.transform(X_woman)

kmeans = KMeans(n_clusters=4)

kmeans.fit(X_man_scaled)
print("Man Cluster memberships:\n{}".format(kmeans.labels_))
print(kmeans.cluster_centers_)

kmeans.fit(X_woman_scaled)
print("Woman Cluster memberships:\n{}".format(kmeans.labels_))
print(kmeans.cluster_centers_)
