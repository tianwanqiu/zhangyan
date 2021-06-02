"""
求圆的面积
A = math.pi * math.pow(self.r, 2)
"""

import math


class GetArea:
    def __init__(self, r):
        self.r = r

    def mj(self):
        A = math.pi * math.pow(self.r, 2)
        # print("圆的面积=%f" % A)
        return A


if __name__ == "__main__":
    mianji = GetArea(3)
    print("圆的面积是：", mianji.mj())
