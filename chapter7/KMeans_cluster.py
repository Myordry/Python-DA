# -*- coding:utf-8 -*-
#KMeans聚类方法

import pandas as pd
from sklearn.cluster import KMeans  ##导入KMeans聚类方法

inputfile = "F:\DeskTop\Python-Data\chapter7\demo\data\zscoreddata.xls"

k = 5 #聚类为5类

data = pd.read_excel(inputfile)

#调用KMeans方法，进行分析
kmodel = KMeans(n_clusters=k,n_jobs=1)  #n_job为并行数，设定为CPU数目较好
kmodel.fit(data) #训练模型

#查看聚类中心以及聚类数目
r1=pd.Series(kmodel.labels_).value_counts()
r2=pd.DataFrame(kmodel.cluster_centers_)
r=pd.concat([r2,r1],axis=1)
r.columns=list(data.columns)+['类别数目']

print(r)