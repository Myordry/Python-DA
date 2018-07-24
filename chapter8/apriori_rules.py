# -*- coding:utf-8 -*-
# import sys
# sys.path.append("D:\PycharmProjects\LuoXM-1\Python-DA\chapter8")
import pandas as pd
from apriori import *  #导入自行编写的apriori函数
import time  ##时间模块，用来计算运行用时


inputfile = r"F:\DeskTop\Python-Data\chapter8\demo\data\apriori.txt"  #事物集文件
data = pd.read_csv(inputfile,header=None,dtype=object)

start = time.clock()
print(u"转换原始数据至0-1矩阵...")
ct = lambda x:pd.Series(1,index=x[pd.notnull(x)]) #转换0-1矩阵的过渡函数
b = list(map(ct,data.as_matrix()))
data = pd.DataFrame(b).fillna(0)  ##空值用0填充
end = time.clock() ##计时结束
print(u"\n转换完成，用时：%0.2f秒" %(end-start))
del b #删除中间变量，节省内存

support = 0.06 #最小支持度
confidence = 0.75 #最小置信度
ms = "----"  #连接符，默认'--'，用来区分不同元素，如A--B。需要保证原始表格中不含有该字符

start = time.clock()
print(u"\n开始搜索关联规则...")
find_rule(data,support,confidence,ms)  ##此处有个sort错误，改为sort_values
end = time.clock()
print(u"\n搜索完成，用时：%0.2f秒" %(end-start))




