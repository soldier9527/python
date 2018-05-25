# -*- coding: utf-8 -*-

def trim(str):
    if str[0:1]==" ":
        return trim(str[1:])
    elif str[-1:] == " ":
        return trim(str[:-1])
    else:
        return str

if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')