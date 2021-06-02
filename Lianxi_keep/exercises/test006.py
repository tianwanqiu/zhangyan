"""
输出 9*9 乘法口诀表
"""


def method001():
    for i in range(1, 10):
        for j in range(1, i+1):
            # 表达式的东西都写在双引号里面，%后面跟上变量
            # 使数据在同一行显示使用end="\t", 换行则使用print("")
            print("%d*%d=%d" % (i, j, i*j), end="\t")
        print("")


if __name__ == "__main__":
    method001()
