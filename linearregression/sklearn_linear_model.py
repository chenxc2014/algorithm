import pandas as pd
import numpy as py
from sklearn import linear_model


df = pd.read_excel("G:\\000_Program\\002_Python\\traindata\\price2area.xlsx")
print(df)

series = df["square_feet"]
array = py.array(series)

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
print(a * x1 + b)

# 方法2：通过模型来预测
x2_array = py.array(x1)
x2 = x2_array.reshape(-1, 1)
y2 = regr.predict(x2)
print(y2)

