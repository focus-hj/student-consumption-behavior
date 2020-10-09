import pandas as pd

data1 = pd.read_csv("../data/data1.csv", encoding='gbk')

# data1数据处理
# print(data1.head(3))
# print(data1.shape)

# 列重命名
data1.columns = ['序号', '校园卡号', '性别', '专业名称', '门禁卡号']
# data1.info()
# print(data1.columns)

# 检查data1每列的缺失值的占比
print(data1.apply(lambda x: sum(x.isnull()) / len(x), axis=0))

print(data1.head(3))

# 将data1存储为task1_1_1.csv
data1.to_csv('../data/out/task1_1_1.csv', index=False, encoding='gbk')
