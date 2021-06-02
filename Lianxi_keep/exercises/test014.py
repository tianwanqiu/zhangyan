"""
两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单
使用permutations 函数进行排序组合
"""

import itertools


def method001():
    for i in itertools.permutations(['x', 'y', 'z'], 3):
        if (i[0] != 'x') and (i[2] != 'x') and (i[2] != 'z'):
            print("a vs %s " % i[0])
            print("b vs %s " % i[1])
            print("c vs %s " % i[2])


if __name__ == "__main__":
    method001()
