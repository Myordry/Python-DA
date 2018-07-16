#-*- coding:utf-8 -*-

#餐饮销量数据统计量分析

from __future__ import print_function
import pandas as pd
"""
在开头加上from __future__ import print_function这句之后，即使在python2.X，使用print就得像python3.X
那样加括号使用。python2.X中print不需要括号，而在python3.X中则需要。
"""

catering_sale = "F:\DeskTop\Python-Data\chapter3\demo\data\catering_sale.xls"  ##导入餐饮数据
data = pd.read_excel(catering_sale,index_col="日期")
data = data[(data["销量"] > 400)&(data["销量"] < 5000)]

"""
DataFrame对象的describe()方法给出一些基本的统计量
"""
statistics = data.describe()  #保存基本量统计

print(statistics)
"""
                销量
count   195.000000
mean   2744.595385
std     424.739407
min     865.000000
25%    2460.600000
50%    2655.900000
75%    3023.200000
max    4065.200000
"""


"""

"""
statistics.loc["range"] = statistics.loc["max"] - statistics.loc["min"] ##极差，最大值与最小值之差
statistics.loc["var"] = statistics.loc["std"]/statistics.loc["mean"]  ##变异系数，度量标准差相对于均值的离中趋势
statistics.loc["dis"] = statistics.loc["75%"] - statistics.loc["25%"]

print(statistics)

"""
                销量
count   195.000000
mean   2744.595385
std     424.739407
min     865.000000
25%    2460.600000
50%    2655.900000
75%    3023.200000
max    4065.200000
range  3200.200000
var       0.154755
dis     562.600000
"""
