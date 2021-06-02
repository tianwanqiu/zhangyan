"""
1、使用lambda来创建匿名函数
"""

from functools import reduce


class LianXi02:
    def __init__(self):
        pass

    def example_01(self):
        sum = lambda x, y: x + y
        l = reduce(sum, [1, 2, 3, 4, 5])
        print(l)


if __name__ == "__main__":
    s = LianXi02()
    s.example_01()
