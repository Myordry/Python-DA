#-*- coding:utf-8 -*-

import pandas as pd
from random import shuffle
from sklearn.metrics import confusion_matrix,roc_curve  ##导入混淆矩阵,ROC曲线函数
import matplotlib.pyplot as plt
from keras.models import Sequential  ##导入神经网络初始化函数
from keras.layers.core import Dense,Activation  ##导入神经网络层函数、激活函数

"""
data.as_matrix()返回ndarray，即返回数组
shuffle()函数用于将所有元素随机排序
"""
datafile = "F:\DeskTop\Python-Data\chapter6\demo\data\model.xls"
data = pd.read_excel(datafile)
data = data.as_matrix()
shuffle(data)

p = 0.8 #训练数据占总数据量的80%
train = data[:int(len(data)*p),:]
test = data[int(len(data)*p):,:]

netfile = "F:\DeskTop\Python-Data\chapter6\demo\data\lm_net.model"  #构建的神经网络模型存储路径

net = Sequential()  ##建立神经网络
net.add(Dense(input_dim=3,units = 10))  ##添加输入层（3节点）到隐藏层（10节点）的连接
net.add(Activation("relu"))  ##隐藏层使用relu激活函数
net.add(Dense(input_dim=10,units = 1))  ##添加隐藏层（10节点）到输出层（1节点）的连接
net.add(Activation("sigmoid"))  ##输出层使用sigmoid激活函数
net.compile(loss="binary_crossentropy",optimizer="adam")  #编译模型，使用adam求解

"""
训练模型，循环1000次
"""
net.fit(train[:,:3],train[:,3],epochs=1000,batch_size=1)
net.save_weights(netfile)

"""
'''这里要提醒的是，keras用predict给出预测概率，predict_classes才是给出预测类别，而且两者的预测结果
都是n x 1维数组，而不是通常的 1 x n'''
"""
predict_result = net.predict_classes(train[:,:3]).reshape(len(train))   ##将预测结果变形为一维数组


cm = confusion_matrix(train[:,3],predict_result)  ##得到混淆矩阵

plt.matshow(cm,cmap = plt.cm.Greens) ##绘制混淆矩阵图，配色风格使用cm.Greens
plt.colorbar()  ##显示颜色标签
# print(cm)
# print(len(cm))
###数据标签
for x in range(len(cm)):
    for y in range(len(cm)):
        plt.annotate(cm[x,y],xy=(x,y),horizontalalignment = "center",verticalalignment = "center")

plt.ylabel("True label")  ##坐标轴标签
plt.xlabel("Predicted label")   ##坐标轴标签
plt.show()

##绘制ROC曲线
predict_result = net.predict(test[:,:3]).reshape(len(test))
fpr,tpr,thresholds = roc_curve(test[:,3],predict_result,pos_label=1)
plt.plot(fpr,tpr,linewidth=2,label="ROC of LM")  ##做出ROC曲线
plt.xlabel('False Positive Rate') #两个坐标轴标签
plt.ylabel('True Positive Rate')
plt.ylim(0,1.05)  ##两个坐标轴范围
plt.xlim(0,1.05)
plt.legend(loc=4)  #图例
plt.show()









