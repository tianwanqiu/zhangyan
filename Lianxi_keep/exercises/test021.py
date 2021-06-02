"""
1、按逗号分隔列表
2、有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中
[1,2,4,5,6], 输入3 插入2 的后面
3、统计 1 到 100 之和
"""


class LianXi01:

    def __init__(self):
        self.li = [1, 2, 3, 4, 5]
        self.li2 = [1, 2, 4, 5]

    def example_01(self):
        s = ','.join(str(i) for i in self.li)  # str.join(sequence), sequence 可以是List 也可以是tuple(元组）
        print(s)

    def example_02(self):
        self.li2.append(3)
        self.li2.sort()
        print(self.li2)

    def example_03(self):
        s = sum(range(1, 101))
        print(s)


if __name__ == "__main__":
    p = LianXi01()  # 调用类中的方法时，必须要实例化一个类的实例
    # p.example_01()
    # p.example_02()
    p.example_03()

