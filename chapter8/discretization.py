# -*- coding:utf-8 -*-
"""
聚类离散化，最后的result的格式为：
      1           2           3           4
A     0    0.178698    0.257724    0.351843
An  240  356.000000  281.000000   53.000000
即(0, 0.178698]有240个，(0.178698, 0.257724]有356个，依此类推。
"""
import pandas as pd
from sklearn.cluster import KMeans  ##用K均值算法进行各个属性的离散化

datafile = "F:\DeskTop\Python-Data\chapter8\demo\data\data.xls"
processedfile = "F:\DeskTop\Python-Data\chapter8\demo\data\data_processed.xls"
typelabel = {u'肝气郁结证型系数':'A', u'热毒蕴结证型系数':'B',
             u'冲任失调证型系数':'C', u'气血两虚证型系数':'D',
             u'脾胃虚弱证型系数':'E', u'肝肾阴虚证型系数':'F'}
k = 4 ##每个属性都聚类为4类

data = pd.read_excel(datafile)
keys = list(typelabel.keys())
"""
print(keys)
['肝气郁结证型系数', '热毒蕴结证型系数',
 '冲任失调证型系数', '气血两虚证型系数', 
 '脾胃虚弱证型系数', '肝肾阴虚证型系数']
"""
result = pd.DataFrame()

"""
print(data[[keys[0]]]) ###只打印一列时，索引如果加上[]则会打印出这个列名字，不加[]的话无列名
print(data[[keys[0],keys[1]]])  ###打印多个列时，必须加上[]，索引为列表形式
print((data[[keys[0],keys[1]]]).as_matrix())  ##as_matrix()将结果转换为矩阵形势
"""


##########################################################
# """
# 下面用单个进行调试
# """
# i = 0
# kmodel = KMeans(n_clusters=k,n_jobs=1)
# kmodel.fit(data[[keys[i]]].as_matrix()) #训练模型
#
# r1 = pd.DataFrame(kmodel.cluster_centers_,columns = [typelabel[keys[i]]]) #聚类中心，列名为症状名对应的字母ABCDEF
# # print(r1)
# """
# 一维聚类，得到四个聚类中心
#           A
# 0  0.295406
# 1  0.137643
# 2  0.221225
# 3  0.408679
# """
# r2 = pd.Series(kmodel.labels_).value_counts()  ##分类统计,打印每类的分类个数
# # print(r2)
# """
# 2    356
# 1    281
# 0    240
# 3     53
# dtype: int64
# """
# r2 = pd.DataFrame(r2,columns=[typelabel[keys[i]]+"n"])  ##转为DataFrame，记录各个类别的数目
# # print(r2)
# """
#     An
# 3  356
# 0  281
# 1  240
# 2   53
# """
# r = pd.concat([r1,r2],axis=1)  #匹配聚类中心和类别数目,concat有自动按照行名匹配的功能
# print(r)
# """"
#           A   An
# 0  0.295406  278
# 1  0.137643  244
# 2  0.408679   53
# 3  0.221225  355
# """
# r = pd.concat([r1,r2],axis=1).sort_values(typelabel[keys[i]])  #匹配聚类中心和类别数目,concat有自动按照行名匹配的功能
# print(r)
# """
#           A   An
# 1  0.136954  240
# 3  0.220441  356
# 0  0.295007  281
# 2  0.408679   53
"""

# """
#           A   An
# 0  0.295007  281
# 1  0.136954  240
# 2  0.408679   53
# 3  0.220441  356
# """
# r.index=[1,2,3,4]  ##将索引值改为1,2,3,4
# print(r)
# """"
#           A   An
# 1  0.137643  244
# 2  0.295007  281
# 3  0.220912  352
# 4  0.408679   53
# """
# r[typelabel[keys[i]]] = pd.rolling_mean(r[typelabel[keys[i]]],2)  ##rolling_mean()用来计算相邻2个聚类点的均值，以此作为边界点
# print(r)
# """"
#           A   An
# 1       NaN  244
# 2  0.216325  281
# 3  0.257960  352
# 4  0.314796   53
# """
# r[typelabel[keys[i]]][1] = 0.0
# print(r)
# """
#           A   An
# 1  0.000000  240
# 2  0.215981  281
# 3  0.257724  356
# 4  0.314560   53
# """
###########################################################




# 接下来调用kmeans算法进行聚类分析
for i in range(len(keys)):
    print("正在进行“%s”的聚类..."% keys[i])
    kmodel = KMeans(n_clusters=k,n_jobs=1)
    kmodel.fit(data[[keys[i]]].as_matrix()) #训练模型


    r1 = pd.DataFrame(kmodel.cluster_centers_,columns = [typelabel[keys[i]]]) #聚类中心，列名为症状名
    r2 = pd.Series(kmodel.labels_).value_counts()  ##分类统计
    r2 = pd.DataFrame(r2,columns=[typelabel[keys[i]]+"n"])  ##转为DataFrame，记录各个类别的数目
    r = pd.concat([r1,r2],axis=1)  #匹配聚类中心和类别数目
    r.index = [1,2,3,4]  ##类名称

    r[typelabel[keys[i]]] = pd.rolling_mean(r[typelabel[keys[i]]],2)  ##rolling_mean()用来计算相邻2个聚类点的均值，以此作为边界点
    r[typelabel[keys[i]]][1] = 0.0
    result = result.append(r.T)

result = result.sort_index() #以Index排序，即以A,B,C,D,E,F顺序排
# result.to_excel(processedfile)
print(result)
""""
正在进行“冲任失调证型系数”的聚类...
正在进行“气血两虚证型系数”的聚类...
正在进行“脾胃虚弱证型系数”的聚类...
正在进行“肝肾阴虚证型系数”的聚类...
        1           2           3           4
A     0.0    0.215981    0.178698    0.314560
An  281.0  240.000000  356.000000   53.000000
B     0.0    0.313383    0.368176    0.284702
Bn  316.0   54.000000  391.000000  169.000000
C     0.0    0.288684    0.245362    0.336551
Cn  393.0  206.000000  296.000000   35.000000
D     0.0    0.214654    0.279951    0.317576
Dn  224.0  283.000000   44.000000  379.000000
E     0.0    0.257873    0.376062    0.270886
En  319.0  245.000000   93.000000  273.000000
F     0.0    0.309463    0.179143    0.224323
Fn  228.0  237.000000  200.000000  265.000000
"""


