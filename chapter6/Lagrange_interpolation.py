#-*- coding:utf-8 -*-
##拉格朗日插值处理数据缺失值

import pandas as pd
from scipy.interpolate import lagrange  ##通过SciPy导入插值函数lagrange

"""
给出源文件的路径和处理后文件的路径，Excel格式
"""
inputfile = "F:\DeskTop\Python-Data\chapter6\demo\data\missing_data.xls"
outputfile = "F:\DeskTop\Python-Data\chapter6\demo\data\missing_data_processed.xls"

"""
读入数据
指定行用来作为列名，数据开始行数。如果文件中没有列名，则默认为0，否则设置为None。如果明确设定
header=0 就会替换掉原来存在列名。header参数可以是一个list例如：[0,1,3]，这个list表示将文件中
的这些行作为列标题（意味着每一列有多个标题），介于中间的行将被忽略掉
"""
data = pd.read_excel(inputfile,header=None)

"""
自定义列向量插值函数
s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
"""
def ployinterp_column(s,n,k=5):
    y = s[list(range(n-k,n)) + list(range(n+1,n+1+k))] ##取前后各五个数组成一个向量
    y = y[y.notnull()]  ##将这十个数中的空值去掉
    return lagrange(y.index,list(y))(n)   ##插值并返回插值结果

#遍历整个数据，找出需要插值的位置并做处理

"""
data.columns打印列名称
data.index为行索引
len(data)为列的长度
data[0]为第一列
data.loc[0]为第一行
"""
# print(data.columns)
# print(len(data))
# print(data[0])
# print(data.loc[0])
# print(data.index)

"""
data.isnull()返回一个向量，是空值的为True,不是空值的为False
"""

for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:  ##如果为空值
            data[i][j] = ployinterp_column(data[i],j)

data.to_excel(outputfile, header=None, index=False) #输出结果

