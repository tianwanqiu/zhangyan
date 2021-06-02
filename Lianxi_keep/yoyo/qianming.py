"""
封装签名函数

字典{},列表[]， 元组()
签名参数sign生成的方法

第1步: 将所有参数（注意是所有参数），除去sign本身，以及值是空的参数，按参数名字母升序排序。
第2步: 然后把排序后的参数按参数1值1参数2值2…参数n值n（这里的参数和值必须是传输参数的原始值，不能是经过处理的，如不能将"转成”后再拼接）的方式拼接成一个字符串。
第3步: 把分配给接入方的验证密钥key拼接在第2步得到的字符串key。
第2步: 在上一步得到的字符串后面加上验证密钥key(这里的密钥key是接口提供方分配给接口接入方的)，然后计算md5值，得到32位字符串，然后转成大写.
第4步: 计算第3步字符串转小写后得到的md5值(32位)，得到的字符串作为sign的值。
"""
import hashlib


def sign_body(body, apikey):
    # 列表生产式，用join 方法连接字符串，if 后面的没看懂
    a = ["".join(i) for i in body.items() if i[1] and i[0] != 'sign']
    print(a)
    # sorted 是对所有可迭代的对象进行，而sort 只能对list 进行排序，而且sort 会改变原始的list
    # 按参数名字母升序排序
    strA = "".join(sorted(a))
    print(strA)
    striSignTemp = strA + apikey

    # 编写md5 加密方法
    def jiamimd5(src):
        m = hashlib.md5()
        m.update(src.encode('UTF-8'))
        return m.hexdigest()

    # 转化为小写，并将其加密
    sign = jiamimd5(striSignTemp.lower())
    print(sign)
    # json 类似与字典，可以通过键取值
    body['sign'] = sign
    return body


if __name__ == "__main__":
    apikey = '12345678'
    body = {
        "username": "lisi",
        "password": "123456A",
        "sign": ""
    }
    print(sign_body(body, apikey))
