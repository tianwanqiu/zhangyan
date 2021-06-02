'''
给你一个字符串，你怎么判断是不是ipv4地址？手写这段代码，并写出测试用例
先要知道 ipv4 地址的格式：(1~255).(0~255).(0~255).(0~255)
'''

import pytest
import re

test_data = [
    [1234, False],
    ["", False],
    ["abcdef", False],
    ["123.456", False],
    ["1.2.3", False],
    ["a.1.1.1", False],
    ["0.1.1.1", False],
    ["1.1.1.1", True],
    ["9.1.1.1", True]

]


def check_ipv4(ip_str):
    """检查ipv4地址格式"""
    if not isinstance(ip_str, str):
        print("输入参数不合法，请输入字符串")
        return False
    if ip_str.count(".") != 3:
        return False
    else:
        ip_list = ip_str.split(".")
        print(ip_list)  # 按点切割四个部分
        # 校验每个部分的合法性，判断是不是数字
        num1 = ip_list[0]
        try:
            n1 = int(num1)
            print("第1个数字:", n1)
            if (n1 >= 1) and (n1 <= 255):
                pass
            else:
                return False
        except:
            return False
        # 后面3个数字
        for n in ip_list[1:]:
            try:
                n2 = int(n)
                print("后面数字:", n2)
                if (n2 >= 0) and (n2 <= 255):
                    pass
                else:
                    return False
            except:
                return False
        return True


def check_ipv4_by_re(ip_str):
    """正则判断ipv4"""
    if not isinstance(ip_str, str):
        print("输入参数不合法，请输入字符串")
        return False
    compile_ipv4 = re.compile(
        '^([1-9]|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))(\\.([0-9]|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))){3}$')
    if compile_ipv4.match(ip_str):
        return True
    else:
        return False


@pytest.mark.parametrize("test_input, expected", test_data)
def test_ip(test_input, expected):
    assert expected == check_ipv4_by_re(test_input)


if __name__ == "__main__":
    # result = check_ip('1.4.5.6')
    # print(result)
    pytest.main(["-s", "test_ip.py"])
