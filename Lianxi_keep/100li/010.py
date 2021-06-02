def get_common_str(list_a):
    '''
    输入列表a，返回公共子串
    输入: ["flower","flow","flight"]
    输出: "fl"
    输入: ["dog","racecar","car"]输出: ""
    '''
    if len(list_a) == 0:
        return ''
    common_str = ''  # 公共字符串，定义一个变量来接受它

    # 先找出最短的字符串
    min_str = min(list_a, key=lambda x: len(x))
    # print(min_str)  # 最短的字符串flow
    for i in range(len(min_str)):
        flag = False  # 退出外部循环标志
        for j in list_a:
            if min_str[i] != j[i]:
                common_str = min_str[:i]
                flag = True
                break
        if flag:
            break

    return common_str


if __name__ == '__main__':
    a = ["flower", "flow", "flight"]
    print(get_common_str(a))
    b = ["dog", "racecar", "car"]
    print(get_common_str(b))
