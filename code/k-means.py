import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

mpl.use('TkAgg')

font = FontProperties(fname="../SimHei.ttf")

X = pd.read_csv('../data/out/task1_3_2.csv', encoding='gbk')
X = X[['性别', '消费总额', '食堂消费占比', '当月用卡总次数', '常去消费地点']]
# X = X[['性别', '消费总额', '食堂消费占比', '当月用卡总次数']]
print(X.head(10))

X['消费总额'] = pd.cut(X['消费总额'], [0, 100, 200, 350, 500, 1000], labels=[-2, -1, 0, 1, 2])
X['食堂消费占比'] = pd.cut(X['食堂消费占比'], [-0.1, 0.7, 0.85, 0.95, 0.99, 1.1], labels=[-2, -1, 0, 1, 2])
X['当月用卡总次数'] = pd.cut(X['当月用卡总次数'], [-1, 20, 60, 100, 150, 350], labels=[-2, -1, 0, 1, 2])

print(X.head(10))

X_man = X[X['性别'] == 0].drop('性别', axis=1)
X_woman = X[X['性别'] == 1].drop('性别', axis=1)

# scores_man = []
# scores_woman = []
# for i in range(2, 10):
#     kmeans = KMeans(n_clusters=i)
#
#     kmeans.fit(X_man)
#     print("Man Cluster memberships:\n{}".format(kmeans.labels_))
#     print(kmeans.cluster_centers_)
#     scores_man.append(metrics.silhouette_score(X_man, kmeans.labels_, metric='euclidean'))
#
#     kmeans.fit(X_woman)
#     print("Woman Cluster memberships:\n{}".format(kmeans.labels_))
#     print(kmeans.cluster_centers_)
#     scores_woman.append(metrics.silhouette_score(X_woman, kmeans.labels_, metric='euclidean'))
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

kmeans = KMeans(n_clusters=4)

kmeans.fit(X_man)
print("Man Cluster memberships:\n{}".format(kmeans.labels_))
print(kmeans.cluster_centers_)

# X_train, X_test, y_train, y_test = train_test_split(X_man, kmeans.labels_, stratify=kmeans.labels_)
# tree = DecisionTreeClassifier(random_state=0)
# tree.fit(X_train, y_train)
# print('Accuracy on training set: {:.3f}'.format(tree.score(X_train, y_train)))
# print('Accuracy on test set: {:.3f}'.format(tree.score(X_test, y_test)))

tree = DecisionTreeClassifier()
scores_man = cross_val_score(tree, X_man, kmeans.labels_)

kmeans.fit(X_woman)
print("Woman Cluster memberships:\n{}".format(kmeans.labels_))
print(kmeans.cluster_centers_)

tree = DecisionTreeClassifier()
scores_woman = cross_val_score(tree, X_woman, kmeans.labels_)

print('Man K-means cross-validation score: {}'.format(np.mean(scores_man)))
print('Woman K-means cross-validation score: {}'.format(np.mean(scores_woman)))
