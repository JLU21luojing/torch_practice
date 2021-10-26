import torch
import numpy as np

#eye方法:生成对角线为1，其他为0的n*m的2维张量
y = torch.eye(3,3)  #参数列表 为n,m,out
print(y)
""""
输出
tensor([[1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]])
"""
#from_numpy方法:使用numpy生成数组，from_numpy将这个数组变成张量，两个变量在同一个内存下，修改任意一个都会改变另一个值
a = np.array([1, 2, 3])
t = torch.from_numpy(a)
print(t)
t[0] = -1
print(a)
a[0] = 1
print(a)
""""
输出
tensor([1, 2, 3], dtype=torch.int32)
[-1  2  3]
[1 2 3]
"""
#linspace方法:生成从start 到 end 间隔 为step的点

print(torch.linspace(-1, 10, 5))

""""
输出
tensor([-1.0000,  1.7500,  4.5000,  7.2500, 10.0000])
"""
#logspace 方法:生成从10start 到 end间隔为step的点