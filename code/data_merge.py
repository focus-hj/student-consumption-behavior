import pandas as pd

data1 = pd.read_csv("../data/out/task1_1_1.csv", encoding="gbk")
data2 = pd.read_csv("../data/out/task1_1_2.csv", encoding="gbk")
data3 = pd.read_csv("../data/out/task1_1_3.csv", encoding="gbk")

print(data1.head(3))
print(data2.head(3))
print(data3.head(3))

data1_merge_data2 = pd.merge(data1, data2, how='left', left_on='校园卡号', right_on='校园卡号')
print(data1_merge_data2.shape)
print(data1_merge_data2.tail(3))

# 检查data1_merge_data2每列的缺失值的占比
print(data1_merge_data2.apply(lambda x: sum(x.isnull()) / len(x), axis=0))

# 缺失值处理，所选列有空即删除该行
print('删除缺失值前：', data1_merge_data2.shape)
data1_merge_data2 = data1_merge_data2.dropna(subset=['消费地点'], how='any')
print('删除缺失值后：', data1_merge_data2.shape)

# 将data1_merge_data2存储为task1_2_1.csv
data1_merge_data2.to_csv('../data/out/task1_2_1.csv', index=False, encoding='gbk')

data1_merge_data3 = pd.merge(data1, data3, how='left', left_on='门禁卡号', right_on='门禁卡号')
print(data1_merge_data3.head(3))

# 检查data1_merge_data3每列的缺失值的占比
print(data1_merge_data3.apply(lambda x: sum(x.isnull()) / len(x), axis=0))

print('删除缺失值前：', data1_merge_data3.shape)
data1_merge_data3 = data1_merge_data3.dropna(subset=['进出地点'], how='any')
print('删除缺失值后：', data1_merge_data3.shape)

# 将data1_merge_data3存储为task1_2_2.csv
data1_merge_data3.to_csv('../data/out/task1_2_2.csv', index=False, encoding='gbk')
