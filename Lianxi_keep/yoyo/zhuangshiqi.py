import time
from functools import wraps

# 此为函数装饰器，必有返回值
# def zhuangshi(func):
#     def neizhi():
#         strat_time = time.time()
#         f = func()
#         end_time = time.time()
#         print("运行时间%.4f" % (end_time - strat_time))
#         return f
#
#     return neizhi
#
#
# @zhuangshi
# def func_a():
#     print("helllo")
#     time.sleep(0.5)
#
#
# @zhuangshi
# def func_b():
#     print("word")
#     time.sleep(0.5)

# 此为类装饰器，带参数得那种
class zhishiqi():
    def __init__(self, slowly=1):
        self.slowly = slowly

    def __call__(self, func):
        @wraps(func) #消除装饰器的影响，正常打印函数中的注释
        def wapper(*args, **kwargs):
            statr_time = time.time()
            f = func(*args, **kwargs)
            end_time = time.time()
            t = end_time-statr_time
            time.sleep((self.slowly-1)*t)  # 延迟时间
            new_end = time.time()
            print("运行时间%.2f" % (new_end - statr_time))
            return f

        return wapper


@zhishiqi(1.5)
def func_a(a):
    """一行注释"""
    print("helllo"+a)
    time.sleep(0.5)


@zhishiqi(2.5)
def func_b(b, c="xx"):
    """b的注释"""
    print("word"+b+c)
    time.sleep(0.5)


if __name__ == "__main__":
    # 函数中有参数，就要有对应得值传进去
    func_a("a")
    print(func_a.__name__)  # 打印正在运行的函数名称
    print(func_a.__doc__)
    func_b("b", c="xxx")
    print(func_b.__name__)
    print(func_b.__doc__)

