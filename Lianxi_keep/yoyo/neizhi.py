"""
内置函数 map()、reduce()、 filter() 的使用
map 和 reduce 函数用于计算可迭代对象，主要区别map 函数的参数可以是一个也可以是多个，但是reduce 的函数参数必须是两个
filter 函数用于过滤可迭代对象
"""

from functools import reduce


class NeiZhi:

    def __init__(self):
        a = [1, 2, 3, 4]
        m = ["张三", "张对", "张武", "王三"]
        self.a = a
        self.m = m

    def test_01(self):
        # 使用列表中“每个值”取余数
        """
        # 方法一
        b = list(map(lambda x: x % 2, self.a))
        print(b)
        """

        def yusu(x):
            return x % 2

        b = list(map(yusu, self.a))  # 这里调用的函数，是不需要有（）的
        print(b)

    def test_02(self):
        # 实现列表各字段值累加
        s = reduce(lambda x, y: x + y, self.a)
        print(s)

    def test_03(self):
        # 实现列表数据过滤
        l = list(filter(lambda x: x < 3, self.a))
        print(l)

        h = list(filter(lambda x: not str(x).startswith("张"), self.m))
        print(h)


if __name__ == "__main__":
    nei = NeiZhi()
    nei.test_03()
