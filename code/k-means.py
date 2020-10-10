import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import mglearn
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

X = pd.read_csv('../data/out/task1_3_2.csv', encoding='gbk')
X = X[['性别', '超市消费总额', '食堂消费总额', '当月用卡总次数', '常去消费地点']]

scaler = MinMaxScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)
print(X)
print(X_scaled)

kmeans = KMeans(n_clusters=4)
# kmeans.fit(X_scaled)
kmeans.fit(X)
print("Cluster memberships:\n{}".format(kmeans.labels_))
print(np.rint(kmeans.cluster_centers_))

