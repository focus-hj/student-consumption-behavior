import pandas as pd

data3 = pd.read_csv("../data/data3.csv", encoding='gbk')

print(data3.head(10))
print(data3.shape)

data3.columns = ['序号', '门禁卡号', '进出时间', '进出地点', '是否通过', '描述']

data3.info()
print(data3.columns)

# 对data3中消费时间数据进行时间格式转换，coerce将无效解析设置为NaT
data3.loc[:, '进出时间'] = pd.to_datetime(data3.loc[:, '进出时间'], format='%Y/%m/%d %H:%M', errors='coerce')
print(data3.head(3)['进出时间'])

# 检查data3每列的缺失值的占比
print(data3.apply(lambda x: sum(x.isnull()) / len(x), axis=0))

# 各消费地点出现的频次
print(data3['进出地点'].value_counts(dropna=False))

# 统计data3信息
print(data3.describe())

# 单独一列的所有值出现的频次
print(data3['是否通过'].value_counts(dropna=False))

# 删除是否通过中值为0的异常值
# 应用查询条件找出正常值，再覆盖原表
querySer = data3.loc[:, '是否通过'] != 0
print('删除异常值之前:', data3.shape)
data3 = data3.loc[querySer, :]
print('删除异常值之后：', data3.shape)

# 将data3存储为task1_1_3.csv
data3.to_csv('../data/out/task1_1_3.csv', index=False, encoding='gbk')
