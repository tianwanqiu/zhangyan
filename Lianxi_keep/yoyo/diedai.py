"""
带有yield的函数被称为生成器
yield与return 不同在于 有yield的函数必须使用next()函数才会有数据返回，而return 是直接返回数据
每调用一次 next() 都会执行到 yield 停止
生成器可以使用for 循环遍历
yield 的作用有2个，第一个是我们上面看到的可以类似于 return ，返回一个值出来。另外一个功能是可以接收外部传过去的值，给 yield 传值需用到send() 方法
有send()就可以不用next()了，但是第一个，但是第一个send(None)必须是None
"""


def function():
    print("start.....")
    s = 1
    while True:
        s += 1
        print("s 的值：", s)
        yield s
        print("yield 后s 的值：", s)


a = function()
print(a)  # <generator object function at 0x000001A039955258>

print(next(a))

# 第二次调用生成器函数，会再重新执行一遍while函数直到yield 结束
print(next(a))
