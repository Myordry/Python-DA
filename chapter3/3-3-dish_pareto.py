#-*- coding: utf-8 -*-
#菜品盈利数据 帕累托图

import pandas as pd
import matplotlib.pyplot as plt

dish_profit = "F:\DeskTop\Python-Data\chapter3\demo\data\catering_dish_profit.xls"
data = pd.read_excel(dish_profit, index_col = u'菜品名')
data = data[u'盈利'].copy()

"""
# data.sort(ascending = False)   
会报错，'Series' object has no attribute 'sort'
"""
data.sort_values(ascending = False)

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

plt.figure()
data.plot(kind="bar")  ###dataframe自带画图函数
plt.ylabel("盈利（元）")
"""
.cumsum()函数的功能是返回给定axis上的累计和
"""
p = 1.0*data.cumsum()/data.sum()
p.plot(color="r",secondary_y=True,style="-o",linewidth=2)
plt.annotate(format(p[6], '.4%'), xy = (6, p[6]), xytext=(6*0.9, p[6]*0.9), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")) #添加注释，
plt.ylabel('盈利（比例）')
plt.show()




