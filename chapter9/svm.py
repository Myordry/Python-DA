# -*- coding:utf-8 -*-
import pandas as pd
from numpy.random import shuffle
from sklearn import svm,metrics ##导入SVM模型和混淆矩阵模型

inputfile = "F:\DeskTop\Python-Data\chapter9\demo\data\moment.csv"  #数据文件路径
outputfile1 = "F:\DeskTop\Python-Data\chapter9\demo\data\cm_train.xls"  #训练样本的混淆矩阵保存路径
outputfile2 = "F:\DeskTop\Python-Data\chapter9\demo\data\cm_test.xls"  #测试样本混淆矩阵保存路径
data = pd.read_csv(inputfile,encoding="gbk")  #指定编码“gbk”
data = data.as_matrix()

"""
#随机打乱数据
选取80%为训练数据，20%为测试数据
"""
shuffle(data)
print(data[:,0])
data_train = data[:int(0.8*len(data)),:]
data_test = data[int(0.8*len(data)):,:]

"""
为了给各个属性提高区分度和准确度，乘以一个系数
太大会导致过拟合
太小会导致区分度低，模型准确度小
反复测试后选取30
"""
x_train = data_train[:,2:]*30
y_train = data_train[:,0].astype(int)
x_test = data_test[:,2:]*30
y_test = data_test[:,0].astype(int)

#训练模型
model = svm.SVC()
model.fit(x_train,y_train)

"""
保存模型，以后可以通过下面语句重新加载模型：
model = pickle.load(open('../tmp/svm.model', 'rb'))
# """
# import pickle
# pickle.dump(model,open("F:\DeskTop\Python-Data\chapter9\demo\data\svm.model","wb"))

cm_train = metrics.confusion_matrix(y_train,model.predict(x_train)) #训练样本的混淆矩阵
cm_test = metrics.confusion_matrix(y_test,model.predict(x_test)) #测试样本的混淆矩阵
print(cm_train)
print(cm_test)

#保存结果
# pd.DataFrame(cm_train, index = range(1, 6), columns = range(1, 6)).to_excel(outputfile1)
# pd.DataFrame(cm_test, index = range(1, 6), columns = range(1, 6)).to_excel(outputfile2)

