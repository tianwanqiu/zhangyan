"""
可变长函数
往函数中以【列表】或者【元组】的形式传递参数时使用：* args
以字典的形式传入参数，使用：**kwargs
"""

def func(*args, **kwargs):
    # print(args)
    print(kwargs)

# func(22,33,a=1)
func(a=1,b=3)