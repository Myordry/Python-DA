#-*- coding: utf-8 -*-
#数据清洗，过滤掉不符合规则的数据

import pandas as pd

datafile = "F:\DeskTop\Python-Data\chapter7\demo\data\\air_data.csv"
cleanfile = "F:\DeskTop\Python-Data\chapter7\demo\data\data_cleaned.csv"

data = pd.read_csv(datafile,encoding="utf-8")

##只保留票价非空值的，每个data["SUM_YR_1"].notnull()返回布尔值的列表，同为True才保留
data = data[data["SUM_YR_1"].notnull() & data["SUM_YR_2"].notnull()]

##只保留票价非零的，或者平均折扣率与总飞行公里数同时为0的记录
index1 = data["SUM_YR_1"] != 0
index2 = data["SUM_YR_2"] != 0
index3 = (data["SEG_KM_SUM"] == 0) & (data["avg_discount"] == 0)
data = data[index1 | index2 |index3]



# data.to_excel(cleanfile)