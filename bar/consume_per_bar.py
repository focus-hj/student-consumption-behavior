import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

mpl.use('TkAgg')

font = FontProperties(fname="../SimHei.ttf")

X = pd.read_csv('../data/out/task1_3_2.csv', encoding='gbk')
X = X[['性别', '消费总额', '当月用卡总次数']]
print(X.head(50))

X['每次刷卡消费均值'] = np.round(X['消费总额'] / X['当月用卡总次数'], decimals=2)
print(X.head(10))

X_man = X[X['性别'] == 0].drop('性别', axis=1)
X_woman = X[X['性别'] == 1].drop('性别', axis=1)

X_man['每次刷卡消费均值'] = pd.cut(X_man['每次刷卡消费均值'], [-1, 2, 3, 4.75, 6, 12], labels=[-2, -1, 0, 1, 2])
X_woman['每次刷卡消费均值'] = pd.cut(X_woman['每次刷卡消费均值'], [-1, 2, 3, 4.5, 6, 12], labels=[-2, -1, 0, 1, 2])

label_list = ['很高(2)', '高(1)', '中(0)', '低(-1)', '很低(-2)']
num_list1 = [len(X_man[X_man['每次刷卡消费均值'] == i]) for i in [2, 1, 0, -1, -2]]
num_list2 = [len(X_woman[X_woman['每次刷卡消费均值'] == i]) for i in [2, 1, 0, -1, -2]]
x = range(len(num_list1))
print(num_list1)
print(num_list2)

rects1 = plt.bar(x=x, height=num_list1, width=0.4, alpha=0.8, color='blue', label='男生')
rects2 = plt.bar(x=[i + 0.4 for i in x], height=num_list2, width=0.4, color='red', label="女生")
plt.xticks([index + 0.2 for index in x], label_list, fontproperties=font)
plt.xlabel('单次消费均值离散值', fontproperties=font)
plt.ylabel('人数', fontproperties=font)
plt.legend(prop=font)

for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")

plt.show()
