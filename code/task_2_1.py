# 绘制各食堂就餐人次的占比饼图，分析学生早中晚餐的就餐地点是否有显著差别，并在报告中进行描述。
# （提示：时间间隔非常接近的多次刷卡记录可能为一次就餐行为）

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties

mpl.use('TkAgg')

font = FontProperties(fname="../SimHei.ttf")

data = pd.read_csv('../data/out/task1_2_1.csv', encoding='gbk')

canteen_name = ['食堂1', '食堂2', '食堂3', '食堂4', '食堂5']

canteen1 = data['消费地点'].apply(str).str.contains('第一食堂').sum()
canteen2 = data['消费地点'].apply(str).str.contains('第二食堂').sum()
canteen3 = data['消费地点'].apply(str).str.contains('第三食堂').sum()
canteen4 = data['消费地点'].apply(str).str.contains('第四食堂').sum()
canteen5 = data['消费地点'].apply(str).str.contains('第五食堂').sum()

man_count = [canteen1, canteen2, canteen3, canteen4, canteen5]

# 创建画布
plt.figure(figsize=(10, 6), dpi=100)

# 绘制饼图
plt.pie(man_count, labels=canteen_name, autopct='%1.2f%%', shadow=False, startangle=90, textprops={'fontproperties': font})

# 显示图例
plt.legend(prop=font)

# 添加标题
plt.title("食堂就餐情况", fontproperties=font)

# 饼图保持圆形
plt.axis('equal')

# 显示图像
plt.show()
