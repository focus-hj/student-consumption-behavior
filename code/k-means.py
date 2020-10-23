import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from collections import defaultdict
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

mpl.use('TkAgg')

font = FontProperties(fname="../SimHei.ttf")

data = pd.read_csv('../data/out/task1_3_2.csv', encoding='gbk')
X = data[['校园卡号', '性别', '专业名称', '消费总额', '食堂消费占比', '中午消费占比', '当月用卡总次数']]
# X = data[['校园卡号', '性别', '专业名称', '消费总额', '食堂消费占比', '中午消费占比', '当月用卡总次数']]

print(X.head(10))
print(X.describe())

X_man = X[X['性别'] == 0]
X_woman = X[X['性别'] == 1]

# 离散化
X_man.loc[:, '消费总额'] = pd.cut(X_man.loc[:, '消费总额'], [0, 80, 200, 380, 500, 1000], labels=[-2, -1, 0, 1, 2])
X_woman.loc[:, '消费总额'] = pd.cut(X_woman.loc[:, '消费总额'], [0, 90, 200, 315, 430, 1000], labels=[-2, -1, 0, 1, 2])
X_man.loc[:, '食堂消费占比'] = pd.cut(X_man.loc[:, '食堂消费占比'], [-0.1, 0.7, 0.85, 0.95, 0.99, 1.1], labels=[-2, -1, 0, 1, 2])
X_woman.loc[:, '食堂消费占比'] = pd.cut(X_woman.loc[:, '食堂消费占比'], [-0.1, 0.7, 0.85, 0.95, 0.99, 1.1], labels=[-2, -1, 0, 1, 2])
X_man.loc[:, '中午消费占比'] = pd.cut(X_man.loc[:, '中午消费占比'], [-0.1, 0.22, 0.33, 0.43, 0.52, 1.1], labels=[-2, -1, 0, 1, 2])
X_woman.loc[:, '中午消费占比'] = pd.cut(X_woman.loc[:, '中午消费占比'], [-0.1, 0.25, 0.36, 0.46, 0.6, 1.1], labels=[-2, -1, 0, 1, 2])
X_man.loc[:, '当月用卡总次数'] = pd.cut(X_man.loc[:, '当月用卡总次数'], [-1, 15, 45, 95, 140, 350], labels=[-2, -1, 0, 1, 2])
X_woman.loc[:, '当月用卡总次数'] = pd.cut(X_woman.loc[:, '当月用卡总次数'], [-1, 20, 55, 95, 130, 350], labels=[-2, -1, 0, 1, 2])
# X_man.loc[:, '每次刷卡消费均值'] = pd.cut(X_man.loc[:, '每次刷卡消费均值'], [-1, 2, 3, 4.75, 6, 12], labels=[-2, -1, 0, 1, 2])
# X_woman.loc[:, '每次刷卡消费均值'] = pd.cut(X_woman.loc[:, '每次刷卡消费均值'], [-1, 2, 3, 4.5, 6, 12], labels=[-2, -1, 0, 1, 2])

print(X_man.head(3))
print(X_woman.head(3))

X_man_train = X_man.drop('性别', axis=1).drop('校园卡号', axis=1).drop('专业名称', axis=1)
X_woman_train = X_woman.drop('性别', axis=1).drop('校园卡号', axis=1).drop('专业名称', axis=1)

print(X_man_train.head(3))
print(X_woman_train.head(3))

# scores_man = []
# scores_woman = []
# for i in range(2, 10):
#     kmeans = KMeans(n_clusters=i)
#
#     kmeans.fit(X_man_train)
#     print("Man Cluster memberships:\n{}".format(kmeans.labels_))
#     print(kmeans.cluster_centers_)
#     scores_man.append(metrics.silhouette_score(X_man_train, kmeans.labels_, metric='euclidean'))
#
#     kmeans.fit(X_woman_train)
#     print("Woman Cluster memberships:\n{}".format(kmeans.labels_))
#     print(kmeans.cluster_centers_)
#     scores_woman.append(metrics.silhouette_score(X_woman_train, kmeans.labels_, metric='euclidean'))
#
# plt.subplot(2, 1, 1)
# plt.plot(range(2, 10), scores_man, marker='o')
# plt.xlabel('Number of clusters')
# plt.ylabel('silhouette_score')
#
# plt.subplot(2, 1, 2)
# plt.plot(range(2, 10), scores_woman, marker='o')
# plt.xlabel('Number of clusters')
# plt.ylabel('silhouette_score')
#
# plt.show()

man_kmeans = KMeans(n_clusters=4)

man_kmeans.fit(X_man_train)
print("Man Cluster memberships:\n{}".format(man_kmeans.labels_))
count_dict1 = defaultdict(int)
for label in man_kmeans.labels_:
    count_dict1[label] += 1
print(count_dict1)
print(man_kmeans.cluster_centers_)

# pca = PCA(n_components=2)
# pca.fit(X_man_train)
# X_man_train_pca = pca.fit_transform(X_man_train)
#
# plt.figure(figsize=(10, 10))
# plt.xlim(X_man_train_pca[:, 0].min(), X_man_train_pca[:, 0].max() + 1)
# plt.ylim(X_man_train_pca[:, 1].min(), X_man_train_pca[:, 1].max() + 1)
# marks = ['.', 'x', '^', 's']
# colors = ['b', 'r', 'g', 'y']
# for i in range(len(X_man_train)):
#     plt.scatter(X_man_train_pca[:, 0], X_man_train_pca[:, 1], c=colors[man_kmeans.labels_[i]], marker=marks[man_kmeans.labels_[i]])
# plt.xlabel("First principle component")
# plt.ylabel("Second principle component")
# plt.show()

tree = DecisionTreeClassifier()
scores_man = cross_val_score(tree, X_man_train, man_kmeans.labels_)

woman_kmeans = KMeans(n_clusters=4)
woman_kmeans.fit(X_woman_train)
print("Woman Cluster memberships:\n{}".format(woman_kmeans.labels_))
count_dict2 = defaultdict(int)
for label in woman_kmeans.labels_:
    count_dict2[label] += 1
print(count_dict2)
print(woman_kmeans.cluster_centers_)

tree = DecisionTreeClassifier()
scores_woman = cross_val_score(tree, X_woman_train, woman_kmeans.labels_)

print('Man K-means cross-validation score: {}'.format(np.mean(scores_man)))
print('Woman K-means cross-validation score: {}'.format(np.mean(scores_woman)))

man_cluster_centers = man_kmeans.cluster_centers_
man_poverty_arg = man_cluster_centers[:, 0].argmin()
major_num_dict = {}
for i, arg in enumerate(man_kmeans.labels_):
    if arg == man_poverty_arg:
        key = X_man.iloc[i, 2]
        if key not in major_num_dict:
            major_num_dict[key] = 1
        else:
            major_num_dict[key] += 1

woman_cluster_centers = woman_kmeans.cluster_centers_
woman_poverty_arg = woman_cluster_centers[:, 0].argmin()
for i, arg in enumerate(woman_kmeans.labels_):
    if arg == woman_poverty_arg:
        key = X_woman.iloc[i, 2]
        if key not in major_num_dict:
            major_num_dict[key] = 1
        else:
            major_num_dict[key] += 1

print(major_num_dict)
print(major_num_dict.keys())
print(major_num_dict.values())
print(len(major_num_dict))

label_list = list(major_num_dict.keys())
num_list1 = list(major_num_dict.values())
num_list2 = [len(X[X['专业名称'] == key]) for key in major_num_dict.keys()]
y = range(len(num_list1))

plt.figure(figsize=(10, 8))
rects1 = plt.barh(y=y, width=num_list1, alpha=0.8, color='red')
rects2 = plt.barh(y=y, width=num_list2, alpha=0.4, color='blue')
plt.yticks(y, label_list, fontproperties=font)
plt.xlabel('贫困生人数', fontproperties=font)
plt.ylabel('专业', fontproperties=font)

for i in range(len(rects1)):
    poverty_num = rects1[i].get_width()
    major_sum = rects2[i].get_width()
    plt.text(major_sum + 0.1, rects2[i].get_y() + rects2[i].get_height() / 2, '%.2f%%' % (poverty_num / major_sum * 100), fontsize=8, ha='left', va='center')

# plt.show()
