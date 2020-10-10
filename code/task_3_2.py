# 根据学生的整体校园消费行为，选择合适的特征，构建聚类模型，分析每一类学生群体的消费特点。

import pandas as pd
from collections import Counter

data = pd.read_csv('../data/out/task1_2_1.csv', usecols=['校园卡号', '性别', '消费金额', '消费次数', '消费类型', '消费地点'], encoding='gbk')
print(data.head(3))
print(data.shape)

# data_new ['校园卡号', '性别', '超市消费总额', '食堂消费总额', '当月用卡总次数', '常去消费地点']
card_num = ''
loc_dict = {}
sex_dict = {}
canteen_dict = {}
market_dict = {}
num_dict = {}

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

    if card_num not in sex_dict:
        sex_dict[card_num] = 0 if row['性别'] == '男' else 1

    if card_num in loc_dict:
        loc_dict[card_num].append(loc)
    else:
        loc_dict[card_num] = [loc]

    if loc == 0:
        if card_num in market_dict:
            market_dict[card_num] += row['消费金额']
        else:
            market_dict[card_num] = row['消费金额']
    else:
        if card_num in canteen_dict:
            canteen_dict[card_num] += row['消费金额']
        else:
            canteen_dict[card_num] = row['消费金额']

    if card_num in num_dict:
        num_dict[card_num].append(row['消费次数'])
    else:
        num_dict[card_num] = [row['消费次数']]

new_data_list = []
for key, value in loc_dict.items():
    collection_value = Counter(value)
    # 常去消费地点编号
    most_common = collection_value.most_common(1)[0][0]
    # 当月用卡总次数
    consume_num = max(num_dict[key]) - min(num_dict[key])
    stu_dict = {'校园卡号': key,
                '性别': sex_dict[key],
                '超市消费总额': market_dict[key] if market_dict.get(key) else 0,
                '食堂消费总额': canteen_dict.get(key) if canteen_dict.get(key) else 0,
                '当月用卡总次数': consume_num,
                '常去消费地点': most_common}
    new_data_list.append(stu_dict)

new_data = pd.DataFrame(new_data_list, columns=['校园卡号', '性别', '超市消费总额', '食堂消费总额', '当月用卡总次数', '常去消费地点'])
print(new_data.head(3))
new_data.to_csv('../data/out/task1_3_2.csv', index=False, encoding='gbk')


