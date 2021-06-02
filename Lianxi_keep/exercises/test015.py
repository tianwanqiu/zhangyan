"""
打印菱形图案
   *
  ***
 *****
*******
 *****
  ***
   *
思考：空格和 * 数量是可以通过 乘以多少来实现的
"""


def method001():
    num = int(input("请输入要打印的行数："))
    n = int((num+1)/2)
    for i in range(1, n+1):
        print(' '*(n-i)+'*'*(i*2-1))
    for j in range(1, n):
        print(' '*j+'*'*((n-1-j)*2+1))


if __name__ == "__main__":
    method001()
