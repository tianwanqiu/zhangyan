"""
1、统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
2、字符串 “axbyczdj”，如果得到结果“abcd”
3、已知一个字符串为“hello_world_yoyo”, 如何得到一个队列 [“hello”,”world”,”yoyo”]
4、已知一个数字为1，如何输出“0001”
"""


class mian_shi():
    def __init__(self):
        li = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
        str_01 = "axbyczdj"
        self.li = li
        self.str_01 = str_01

    def pass_01(self):
        z = [i for i in self.li if i >= 0]
        print("列表中正数个数为：%s" % len(z))
        f = [i for i in self.li if i < 0]
        print("列表中负数个数为：%s" % len(f))

    def pass_02(self):
        # 最简洁方式
        print(self.str_01[::2])
        """
        s1 = []
        for j in range(0, len(self.str_01)):
            if j % 2 == 0:
                s1.append(self.str_01[j])
        s2 = ''.join(s1)
        print(s2)
        """

    def pass_03(self):
        a = "hello_world_zhangyan"
        b = a.split("_")
        print(b)
        c = 1
        print("%04d" % c)  # 格式化输出


if __name__ == "__main__":
    ms = mian_shi()
    ms.pass_03()
