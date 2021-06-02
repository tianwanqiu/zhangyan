"""
求1+2!+3!+...+20!的和, ! 就是阶乘的意思，5！=5*4*3*2*1
"""

l = range(1, 4)


def f(x):
    num = 1
    for i in range(1, x + 1):
        num = num * i
    return num


# map函数的用法，对每个列表中的数据在函数中计算一下然后输出
s = sum(map(f, l))
print(s)
