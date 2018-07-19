#-*- coding:utf-8 -*-

import pandas as pd
from random import shuffle
from sklearn.metrics import confusion_matrix,roc_curve  ##导入混淆矩阵,ROC曲线函数
from sklearn.tree import DecisionTreeClassifier ##导入决策树模型
from sklearn.externals import joblib  ##导入用来保存模型的模块
import matplotlib.pyplot as plt

datafile = "F:\DeskTop\Python-Data\chapter6\demo\data\model.xls"
data = pd.read_excel(datafile)
data = data.as_matrix()
shuffle(data)

p = 0.8 #训练数据占总数据量的80%
train = data[:int(len(data)*p),:]
test = data[int(len(data)*p):,:]

#构建cart决策树模型
treefile = "F:\DeskTop\Python-Data\chapter6\demo\data\lm_tree.model"
tree = DecisionTreeClassifier()
tree.fit(train[:,:3],train[:,3])
##保存模型
joblib.dump(tree,treefile)

"""
Scikit-Learn使用predict方法直接给出预测结果
"""
predict_result = tree.predict(train[:,:3])
cm = confusion_matrix(train[:,3],predict_result)  ##得到混淆矩阵
plt.matshow(cm,cmap = plt.cm.Greens) ##绘制混淆矩阵图，配色风格使用cm.Greens
plt.colorbar()  ##显示颜色标签

###数据标签
for x in range(len(cm)):
    for y in range(len(cm)):
        plt.annotate(cm[x,y],xy=(x,y),horizontalalignment = "center",verticalalignment = "center")

plt.ylabel("True label")  ##坐标轴标签
plt.xlabel("Predicted label")   ##坐标轴标签
plt.show()

##绘制ROC曲线
predict_result = tree.predict(train[:,:3])
fpr,tpr,thresholds = roc_curve(train[:,3],predict_result,pos_label=1)
plt.plot(fpr,tpr,linewidth=2,label="ROC of LM")  ##做出ROC曲线
plt.xlabel('False Positive Rate') #两个坐标轴标签
plt.ylabel('True Positive Rate')
plt.ylim(0,1.05)  ##两个坐标轴范围
plt.xlim(0,1.05)
plt.legend(loc=4)  #图例
plt.show()


