#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==============================================================================
#
# Author        : iaiting
#
# Contact       : iaiting@aliyun.com 88888888@qq.com 186-8888-8888
#
# Generate Data : 2018-03-22
#
# Copyright     : 本文件隶属iaiting，欢迎转载无须知会
#
# Desciption    : Python基础教程（第2版）第4章书本例题
#
# ==============================================================================


# 字典的创建
# ==============================================================================
def chap0402_01():
    phonebook = {'Alice': '1234', "Beth": "2345", 'Cecil': '3456'}
    print(phonebook)


# 通过元组列表创建字典
# ==============================================================================
def chap0402_02():
    list_items = [('name', 'Gumby'), ('age', 33)]
    print(list_items)

    dict_items = dict(list_items)
    print(dict_items)


# 通过关键字参数创建字典
# ==============================================================================
def chap0402_03():
    dict_items = dict(name="qwe123", age=31)
    print(dict_items)

    dict_items2 = dict(dict_items)
    # dict_items2 = dict_items
    print(dict_items2)

    dict_items2['name'] = "123abc"
    print("dict_itmes2 = ", dict_items2)
    print("dict_itmes = ", dict_items)


# 字典格式化字符串
# ==============================================================================
def chap0402_04():
    phonebook = {'Beth': '1234', 'Cecil': '2345', "Alice": "5678"}
    print("Beth's phone number is %(Beth)s" % phonebook)
    print("Alice's phone number is %(Alice)s" % phonebook)
    print("Cecil's phone number is %(Cecil)s" % phonebook)

    print('''\nBeth's phone number is %(Beth)s
Cecil's phone number is %(Cecil)s
Alice's phone number is %(Alice)s''' % phonebook)


# 清空字典
# ==============================================================================
def chap0402_05():
    d = {}
    d['name'] = 'Gumby'
    d['age'] = 34
    print("dict value = ", d)
    dict_rv = d.clear()
    print("dict value = ", d)
    print("dict return value = ", dict_rv)


# 清空字典的用途
# ==============================================================================
def chap0402_06():
    x = {}
    y = x
    x['key'] = 'value'
    print("y =  ", y)
    x = {}
    print("y =  ", y)
    x = y
    x.clear()
    print("y =  ", y)


# 字典浅copy,原地修改值，源副本都将发生变化
# ==============================================================================
def chap0402_07():
    x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
    y = x.copy()
    y['username'] = '123qwe'

    print('x = ', x)
    print('y = ', y)

    x['machines'].remove('foo')
    print('x = ', x)
    print('y = ', y)


# 字典深copy,原地修改值，只变化修改的那个字典
# ==============================================================================
def chap0402_08():
    from copy import deepcopy
    d = {}
    d['names'] = ['Alfred', 'Bertrand']
    print('d = ', d)

    dc = d.copy()
    print('dc = ', dc)

    ddc = deepcopy(d)
    print('ddc = ', ddc)

    d['names'].append('Clive')
    print('d = ', d)
    print('dc = ', dc)
    print('ddc = ', ddc)


# 用指定的键创建值为None的字典
# ==============================================================================
def chap0402_09():
    d1 = {}.fromkeys(['name', 'age'])
    print("d1 = ", d1)

    d2 = dict.fromkeys(['name', 'age'])
    print("d2 = ", d2)

    d3 = dict.fromkeys(['name', 'age'], ('unknown', 'ab'))
    print("d3 = ", d3)


# 字典get获取键值的方法
# ==============================================================================
def chap0402_10():
    d = {}
    ditem_v1 = d.get('name')
    print('ditem_v1 = ', ditem_v1)

    ditem_v2 = d.get('name', 'N/A')
    print('ditem_v2 = ', ditem_v2)


# has_key方法，相当于 k in d python3中没有此方法
# ==============================================================================
# def chap0402_11():
#     d = {}
#     if d.has_key('name'):
#         print('has key')
#     else:
#         print('not has key')


# items 方法 不同版本的python可能有区别
# ==============================================================================
def chap0402_12():
    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
    print('d = ', d)
    l = d.items()
    print('l = ', l, type(l))


# keys 方法
# ==============================================================================
def chap0402_13():
    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
    print('d = ', d)
    l = d.keys()
    print('l = ', l, type(l))


# pop 方法
# ==============================================================================
def chap0402_14():
    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
    print('d = ', d)
    rv = d.pop('title')
    print('d = ', d)
    print('rv = ', rv)


# popitem 方法
# ==============================================================================
def chap0402_15():
    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
    print('d = ', d)
    rv = d.popitem()
    print('d = ', d)
    print('rv = ', rv)


# setdefault 方法
# ==============================================================================
def chap0402_16():
    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
    print('d = ', d)
    rv = d.setdefault('title')
    print('rv = ', rv)
    print('d = ', d)

    rv = d.setdefault('title2')
    print('rv = ', rv)
    print('d = ', d)


# update 方法
# ==============================================================================
def chap0402_17():
    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
    print('d = ', d)

    ud ={'title':'Python Language Website'}
    rv = d.update(ud)

    print('rv = ', rv)
    print('d = ', d)

# update 方法
# ==============================================================================
def chap0402_18():
    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
    print('d = ', d)
    rv = d.values()
    print('rv = ', rv, type(rv))
    print('d = ', d)

# 第2章原生例题
# 通过关键字参数创建字典
# ==============================================================================
def Chap0401():
    people = {
        'Alice': {
            'phone': '1234',
            'addr': 'beijin',
        },
        'Beth': {
            'phone': '1234',
            'addr': 'beijin',
        },
        'Cecil': {
            'phone': '1234',
            'addr': 'beijin',
        }
    }

    labels = {'phone': 'phone number', 'addr': 'address'}
    name = input('Please input your name:')
    request = input('Phone number(p) or address (a)?')

    if request == 'p':
        key = 'phone'
    elif request == 'a':
        key = 'addr'

    if name in people:
        print(("%s's %s is %s") % (name, labels[key], people[name][key]))


# get方法的应用
# ==============================================================================
def Chap0402():
    people = {
        'Alice': {
            'phone': '1234',
            'addr': 'beijin',
        },
        'Beth': {
            'phone': '1234',
            'addr': 'beijin',
        },
        'Cecil': {
            'phone': '1234',
            'addr': 'beijin',
        }
    }
    labels = {'phone': 'phone number', 'addr': 'address'}
    name = input('Name: ')
    request = input('Phone number (p) or address (a)')
    key = request

    if request == 'p': key = 'phone'
    if request == 'a': key = 'addr'

    person = people.get(name, {})
    label = labels.get(key, key)
    result = person.get(key, 'not available')

    print("%s's %s is %s" % (name, label, result))

# ==============================================================================
def Chap04_test():
    chap0402_01()
    chap0402_02()
    chap0402_03()
    chap0402_04()
    chap0402_05()
    chap0402_06()
    chap0402_07()
    chap0402_08()
    chap0402_09()
    chap0402_10()
    # chap0402_11()
    chap0402_12()
    chap0402_13()
    chap0402_14()
    chap0402_15()
    chap0402_16()
    chap0402_17()
    chap0402_18()


#***************************************************************************
# Chap0401()
# Chap0402()

# ==============================================================================
if __name__ == '__main__':
    Chap04_test()
