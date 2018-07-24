# -*- coding:utf-8 -*-
#标准差标准化

import pandas as pd

datafile = "F:\DeskTop\Python-Data\chapter7\demo\data\\zscoredata.xls"
zscorefile = "F:\DeskTop\Python-Data\chapter7\demo\data\zscoreddata.xls"

#标准化处理
data = pd.read_excel(datafile)
data = (data - data.mean(axis=0))/(data.std(axis=0))

data.columns = ["Z"+i for i in data.columns] ##表头重新命名，前面加上Z

# data.to_excel(zscorefile,index=False)

