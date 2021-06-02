"""
假设你有无限数量的邮票,面值分别为6角，7角，8角,请问你最大的不可支付邮资是多少元？
假设你有分别有一张6,7,8的钱币，可以支付的金额就是6,7,8,13,14,15,21。
不可以支付的就是反义词咯，1,2,3,4,5,9,16,17,18,19,20，以及大于22的所有数。那么最大的不可支付的金额就是无穷大咯。
那要是有无穷多的6,7,8，很显然可以支付无穷大的金额咯，那么最大的不可支付金额就不是无穷大，那到底是多少呢？小学三年级的奥数题！
"""


class XiTi001:

    def __init__(self):
        self.a = 6
        self.b = 7
        self.c = 8
        self.t = 50
        self.s = []

    def method(self):
        # 列出所有排列组合
        for i in range(self.t+1):
            s1 = self.a*i
            self.s.append(s1)
            for j in range(self.t+1):
                s2 = self.b*1
                self.s.append(s2)
                for k in range(self.t+1):
                    s3 = self.a*i + self.b*j + self.c*k
                    self.s.append(s3)
        # 排序后去重
        self.s.sort()
        news = list(set(self.s))
        print("组合中生成的最大数%s" % news[-1])
        # 提取不在组合列表中的数据
        r = []
        for i in range(6*self.t):
            if i in news:
                pass
            else:
                r.append(i)
        print("组合中不能生成的数字%s" % r)
        print("不能支付的最大值%s" % r[-1])


if __name__ == "__main__":
    x = XiTi001()
    x.method()
