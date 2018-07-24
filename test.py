#-*- coding: utf-8 -*-
import pandas as pd

inputfile = "F:\DeskTop\Python-Data\chapter9\demo\data\moment.csv"  #数据文件路径
data = pd.read_csv(inputfile, encoding = 'gbk') #读取数据，指定编码为gbk
data = data.as_matrix()
# print(len(data))
# # print(data[:,0])
# data = list(data[:,0])
# print(data.count(1))
# print(data.count(2))
# print(data.count(3))
# print(data.count(4))
# print(data.count(5))

from numpy.random import shuffle #引入随机函数
shuffle(data) #随机打乱数据
print(len(data))
# print(data[:,0])
data = list(data[:,0])
print(data.count(1))
print(data.count(2))
print(data.count(3))
print(data.count(4))
print(data.count(5))

