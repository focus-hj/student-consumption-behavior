# 通过食堂刷卡记录，分别绘制工作日和非工作日食堂就餐时间曲线图，分析食堂早中晚餐的就餐峰值，并在报告中进行描述。

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd

mpl.use('TkAgg')
font = FontProperties(fname="../SimHei.ttf")

data = pd.read_csv('../data/out/task1_2_1.csv', encoding='gbk')

# 对data中消费时间数据进行时间格式转换，转换后可作运算，coerce将无效解析设置为NaT
data.loc[:, '消费时间'] = pd.to_datetime(data.loc[:, '消费时间'], format='%Y-%m-%d %H:%M', errors='coerce')
# print(data.dtypes)

# 创建一个消费星期列，根据消费时间计算出消费星期，Monday=1, Sunday=7
data['消费星期'] = data['消费时间'].dt.dayofweek + 1
print(data.head(3))

# 以周一至周五作为工作日，周六日作为非工作日，拆分为两组数据
work_day_query = data.loc[:, '消费星期'] <= 5
unwork_day_query = data.loc[:, '消费星期'] > 5

work_day_data = data.loc[work_day_query, :]
unwork_day_data = data.loc[unwork_day_query, :]

# 计算工作日消费时间对应的各时间的消费次数，apply()可以将括号里的所有功能应用于前者
work_day_time = []
for i in range(24):
    work_day_time.append(work_day_data['消费时间'].apply(str).str.contains(' {:02d}:'.format(i)).sum())

# 计算非工作日消费时间对应的各时间的消费次数
unwork_day_time = []
for i in range(24):
    unwork_day_time.append(unwork_day_data['消费时间'].apply(str).str.contains(' {:02d}:'.format(i)).sum())

# 以时间段作为x轴，同一时间段出现的次数和作为y轴，作曲线图
x = []
for i in range(24):
    x.append('{:02d}:00'.format(i))

plt.plot(x, work_day_time, label='工作日')
plt.plot(x, unwork_day_time, label='非工作日')
plt.xlabel('时间', fontproperties=font)
plt.ylabel('次数', fontproperties=font)
plt.title('工作日/非工作日消费对比曲线图', fontproperties=font)
plt.xticks(rotation=60)
plt.legend(prop=font)
plt.grid()

plt.show()
