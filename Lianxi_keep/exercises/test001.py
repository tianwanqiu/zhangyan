"""
001题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少
"""
import itertools

s = [1, 2, 3, 4]


# 我写的
def method01():
    n = 0
    for a in s:
        for b in s:
            for c in s:
                if (a != b) and (a != c) and (b != c):
                    print("%d%d%d" % (a, b, c))
                    n = n + 1
    print("共有%d组数据" % n)


def method002():
    n = 0
    for j in range(1, 5):
        for k in range(1, 5):
            for l in range(1, 5):
                # and 之间使用括号括起来， != 是不等于
                if (j != k) and (j != l) and (k != l):
                    # %d 使用引号引起来
                    print("%d%d%d" % (j, k, l), end="\t")
                    n = n + 1
                    print(" ")
    print("total %d" % n)


# 迭代器
def method03():
    n = 0
    for i in itertools.permutations(s, 3):
        print("%d%d%d" % (i[0], i[1], i[2]))
        n = n + 1
    print("共%d组" % n)


if __name__ == "__main__":
    method03()
