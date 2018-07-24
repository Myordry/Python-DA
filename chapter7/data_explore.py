# -*- coding:utf-8 -*-
"""
d对数据进行基本的探索，返回缺失值个数以及最大值最小值等
"""

import pandas as pd

datafile = "F:\DeskTop\Python-Data\chapter7\demo\data\\air_data.csv"  #原始数据
resultfile = "F:\DeskTop\Python-Data\chapter7\demo\data\explore.xls"   #数据探索结果总结表

data = pd.read_csv(datafile,encoding = "utf-8")  #读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）

"""
包括对数据的基本描述，percentiles参数是指定计算多少的分位数表
（如1/4分位数、中位数等）；T是转置，转置后更方便查
"""
explore = data.describe(percentiles=[],include="all").T

#describe()函数自动计算非空值数，需要手动计算空值数
explore["null"] = len(data) - explore["count"]

explore = explore[["null","max","min"]]
explore.columns = [u"空数值",u"最大值",u"最小值"] #对结果统计的表头重命名
"""
'''这里只选取部分探索结果。
describe()函数自动计算的字段有count（非空值数）、unique（唯一值数）、
top（频数最高者）、freq（最高频数）、mean（平均值）、std（方差）、min（最小值）、50%（中位数）、max（最大值）'''
"""
print(explore)

# explore.to_excel(resultfile) ##导出结果



