"""
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
"""
import math


def method001():
    for i in range(-100, 1000):
        x = math.sqrt(i + 100) % 1
        y = math.sqrt(i + 268) % 1
        if (x == 0) and (y == 0):
            print(i)


if __name__ == "__main__":
    method001()
