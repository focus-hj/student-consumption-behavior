import pandas as pd

data2 = pd.read_csv("../data/data2.csv", encoding='gbk')

# data2数据处理
# print(data2.head(3))
# print(data2.shape)
# 列重命名
data2.columns = ['流水号', '校园卡号', '校园卡编号', '消费时间', '消费金额', '存储金额', '余额', '消费次数', '消费类型', '消费项目编码', '消费项目序列号', '消费操作编码',
                 '操作编码', '消费地点']

# data2.info()
# print(data2.columns)

# 对data2中消费时间数据进行时间格式转换，coerce将无效解析设置为NaT
data2.loc[:, '消费时间'] = pd.to_datetime(data2.loc[:, '消费时间'], format='%Y/%m/%d %H:%M', errors='coerce')
print(data2.head(3)['消费时间'])

# 检查data2每列的缺失值的占比
print(data2.apply(lambda x: sum(x.isnull()) / len(x), axis=0))

# 由于消费项目序列号、消费操作编码的缺失值过多，所以不加入后续分析
data2_new = data2[['流水号', '校园卡号', '校园卡编号', '消费时间', '消费金额', '存储金额', '余额', '消费次数',
                   '消费类型', '消费项目编码', '操作编码', '消费地点']]

# 各消费地点出现的频次
print(data2['消费地点'].value_counts(dropna=False))

# 统计data2_new信息
print(data2_new.describe())


# 异常值删除函数
def f(data, col):
    q1 = data[col].quantile(q=0.25)
    q3 = data[col].quantile(q=0.75)
    iqr = q3 - q1
    t1 = q1 - 3 * iqr
    t2 = q3 + 3 * iqr
    return data[(data[col] > t1) & (data[col] < t2)]


# 删除异常值
exception = ['消费金额', '余额', '消费次数']
for i in exception:
    data2_new = f(data2_new, i)
print(data2_new.describe())

# 将data2_new存储为task1_1_2.csv
data2_new.to_csv('../data/out/task1_1_2.csv', index=False, encoding='gbk')
