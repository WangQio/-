import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-2, 2, 50)#起始值为-2，终值为2，生成50个等差数列
print(x1)
y1 = 2*x1 + 1
plt.plot(x1, y1) #绘制曲线
ax = plt.gca()#获取当前影像

#plt.show()

x=np.arange(0,2*np.pi,0.01)#半径范围
y=np.sin(x)

ax.spines['bottom'].set_position(('data',0)) 
ax.spines['left'].set_position(('data',0))#建立坐标轴
plt.plot(x1,y1,x,y)#输出图像
plt.show()