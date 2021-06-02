"""
打印数字区间里面的素数
重解决问题的角度，定义函数
"""


def is_primes(number):
    if number in (1, 2):
        return True
    for idx in range(2, number):
        if number % idx == 0:
            return False
    return True


def print_primes(begin, end):
    for number in range(begin, end + 1):
        if is_primes(number):
            # 可以使用大括号来引用变量,判断函数为ture才会执行
            print(f"{number} is primes")


begin = 11
end = 25
print_primes(begin, end)
