import numpy as np
import matplotlib.pyplot as plt

# 定义 x 的范围
x = np.linspace(-2, 2, 1000)

# 计算 tanh 值
tanh_values = np.tanh(x)

# 计算 tanh 的导数 (1 - tanh^2(x))
derivative_values = 1 - tanh_values ** 2

# 绘制 tanh 函数
plt.plot(x, tanh_values, label='tanh(x)')

# 绘制 tanh 的导数
plt.plot(x, derivative_values, label='derivative of tanh(x)')

# 设置图例
plt.legend()

# 设置标题和轴标签
plt.title('Tanh Function and Its Derivative')
plt.xlabel('x')
plt.ylabel('y')

# 显示图形
plt.grid(True)
plt.show()
