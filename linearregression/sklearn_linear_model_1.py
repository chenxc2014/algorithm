# 线性方程z=a∗x+b∗y+c 表示空间一平面
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D

array_param0 = np.linspace(0, 10, 10)
array_parm1 = np.linspace(0, 100, 10)
array_param2 = np.random.randint(0, 100, (10, 10))

array_xv, array_yv = np.meshgrid(array_param0, array_parm1)
array_zv = 1.0 * array_xv + 3.5 * array_yv + array_param2

# 构建成特征、值的形式
X, Z = np.column_stack((array_xv.flatten(), array_yv.flatten())), array_zv.flatten()

# 建立线性回归模型
regr = linear_model.LinearRegression()
# 拟合
regr.fit(X, Z)
# 得到平面的 系数、截距
a, b = regr.coef_, regr.intercept_

# 给出待预测的一个特征
x1 = np.array([[5.8, 78.3]])

# 方法1：根据线性方程计算出z值
z1 = np.sum(a * x1) + b
# 方法2：根据模型预测出z值
z2 = regr.predict(x1)

# 画图
fig = plt.figure()
ax = fig.gca(projection='3d')

# 画出真实的点
ax.scatter(array_xv, array_yv, array_zv)
# 画出拟合的平面
ax.plot_wireframe(array_xv, array_yv, regr.predict(X).reshape(10, 10))
ax.plot_surface(array_xv, array_yv, regr.predict(X).reshape(10, 10), alpha=0.3)

plt.show()
