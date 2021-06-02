"""
计算前N个数字的平方和
"""

import math


def sum_squer(n):
    result = 0
    for i in range(1, n + 1):
        result += math.pow(i, 2)
    return result


print("3平方和的值：", sum_squer(3))
print("5平方和的值：", sum_squer(5))
print("10平方和的值：", sum_squer(10))
