# 根据学生的整体校园消费行为，选择合适的特征，构建聚类模型，分析每一类学生群体的消费特点。

import pandas as pd
import numpy as np
from collections import Counter
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import mglearn
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

data = pd.read_csv('../data/out/task1_2_1.csv', usecols=['校园卡号', '消费金额', '消费类型', '消费地点'], encoding='gbk')
print(data.head(3))
print(data.shape)

# data_new {'校园卡号': ['消费总额', '常去消费地点']}
card_num = ''
loc_dict = {}
money_dict = {}
for index, row in data.iterrows():
    if row['消费类型'] != '消费':
        continue
    card_num = row['校园卡号']
    loc = 0
    if row['消费地点'] == '第一食堂':
        loc = 1
    elif row['消费地点'] == '第二食堂':
        loc = 2
    elif row['消费地点'] == '第三食堂':
        loc = 3
    elif row['消费地点'] == '第四食堂':
        loc = 4
    elif row['消费地点'] == '第五食堂':
        loc = 5
    else:
        loc = 0
    if card_num in loc_dict:
        loc_dict[card_num].append(loc)
        money_dict[card_num] += row['消费金额']
    else:
        loc_dict[card_num] = [loc]
        money_dict[card_num] = row['消费金额']

new_data = {}
for key, value in loc_dict.items():
    collection_value = Counter(value)
    most_common = collection_value.most_common(1)[0][0]
    new_data[key] = [money_dict[key], most_common]

X = np.array(list(new_data.values()))

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


