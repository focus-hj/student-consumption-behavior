import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

mpl.use('TkAgg')

font = FontProperties(fname="../SimHei.ttf")

X = pd.read_csv('../data/out/task1_3_2.csv', encoding='gbk')
X = X[['性别', '常去消费地点']]
print(X.head(10))

X_man = X[X['性别'] == 0].drop('性别', axis=1)
X_woman = X[X['性别'] == 1].drop('性别', axis=1)

label_list1 = ['第一食堂(1)', '第二食堂(2)', '第三食堂(3)', '第四食堂(4)', '第五食堂(5)', '其它(0)']
num_list1_1 = [len(X_man[X_man['常去消费地点'] == i]) for i in [1, 2, 3, 4, 5, 0]]
num_list1_2 = [len(X_woman[X_woman['常去消费地点'] == i]) for i in [1, 2, 3, 4, 5, 0]]
x = range(len(num_list1_1))
print(num_list1_1)
print(num_list1_2)

rects1 = plt.bar(x=x, height=num_list1_1, width=0.4, alpha=0.8, color='blue', label='男生')
rects2 = plt.bar(x=[i + 0.4 for i in x], height=num_list1_2, width=0.4, color='red', label="女生")
plt.xticks([index + 0.2 for index in x], label_list1, fontproperties=font)
plt.xlabel('常去消费地点', fontproperties=font)
plt.ylabel('人数', fontproperties=font)
plt.legend(prop=font)

for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")

plt.show()
