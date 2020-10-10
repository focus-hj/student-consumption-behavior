import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

mpl.use('TkAgg')

font = FontProperties(fname="../SimHei.ttf")

X = pd.read_csv('../data/out/task1_3_2.csv', encoding='gbk')
X = X[['性别', '超市消费总额', '食堂消费总额', '当月用卡总次数', '常去消费地点']]
print(X.head(10))

scaler = StandardScaler()
scaler.fit(X[['超市消费总额', '食堂消费总额', '当月用卡总次数']])
X.loc[:, ['超市消费总额', '食堂消费总额', '当月用卡总次数']] = scaler.transform(X[['超市消费总额', '食堂消费总额', '当月用卡总次数']])
print(X.head(10))

X['超市消费总额'] = pd.cut(X['超市消费总额'], 5, labels=[-2, -1, 0, 1, 2])
X['食堂消费总额'] = pd.cut(X['食堂消费总额'], 5, labels=[-2, -1, 0, 1, 2])
X['当月用卡总次数'] = pd.cut(X['当月用卡总次数'], 5, labels=[-2, -1, 0, 1, 2])

print(X.head(10))

X_man = X[X['性别'] == 0].drop('性别', axis=1)
X_woman = X[X['性别'] == 1].drop('性别', axis=1)

kmeans = KMeans(n_clusters=4)

kmeans.fit(X_man)
print("Man Cluster memberships:\n{}".format(kmeans.labels_))
print(kmeans.cluster_centers_)

kmeans.fit(X_woman)
print("Woman Cluster memberships:\n{}".format(kmeans.labels_))
print(kmeans.cluster_centers_)
