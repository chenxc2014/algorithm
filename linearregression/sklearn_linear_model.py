# 线性方程y=a∗x+b 表示平面一直线
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


df = pd.read_excel("G:\\000_Program\\002_Python\\traindata\\price2area.xlsx")
print(df)

series = df["square_feet"]
array = np.array(series)

x = array.reshape(-1, 1)
y = df["price"]

# 建立一个线性回归模型
regr = linear_model.LinearRegression()
# 拟合
regr.fit(x, y)
# 得到直线y=a*x+b的系数a、y轴截距b
a, b = regr.coef_, regr.intercept_

# 指定面积 area，预测得到price
x1 = 1000
# 方法1：直接通过直线方程求得
y1 = a * x1 + b
print(y1)

# 方法2：通过模型来预测
x2_array = np.array(x1)
x2 = x2_array.reshape(-1, 1)
y2 = regr.predict(x2)
print(y2)

# 画图
# 画出训练数据中真实的点
plt.scatter(df["square_feet"], df["price"], edgecolors="blue")
# 画出拟合的直线
series = df["square_feet"]
array = np.array(series)
plt.plot(df["square_feet"], regr.predict(array.reshape(-1, 1)), color="red", linewidth=4)
plt.show()

