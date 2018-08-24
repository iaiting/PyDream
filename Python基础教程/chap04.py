#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# Author        : iaiting
#
# Contact       : iaiting@aliyun.com 88888888@qq.com 186-8888-8888
#
# Generate Data : 2018-03-22
#
# Copyright     : 本文件隶属iaiting，欢迎转载无须知会
#
# Desciption    : Python基础教程（第2版）
#                 - 第 4 章 字典: 当索引不好用时
#
################################################################################

################################################################################
def chap0402_01():
    '''
    创建字典
    '''
    phonebook = {'Alice': '1234', "Beth": "2345", 'Cecil': '3456'}
    print("chap0402_01 :\n字典phonebook = {0}\n".format(phonebook))

################################################################################
def chap0402_02(l=None):
    '''
    通过元组列表（键值对序列）创建字典
    '''
    if l is None:
        l_items = [('name', 'Gumby'), ('age', 33)]
    else:
        l_items = l        
    d_items = dict(l_items)
    print("chap0402_02 :")
    print("原始列表 = {0}".format(l_items))
    print("新建字典 = {0}".format(d_items))
    print("")

################################################################################
def chap0402_03():
    '''
    通过关键字参数创建字典
    '''
    d_items = dict(name="qwe123", age=31)
    d_d_items = dict(d_items)
    print("chap0402_03 :")
    print("通过关键字创建的新字典 = {0}".format(d_items))
    print("通过字典创建的新字典 = {0}".format(d_d_items))
    print("")


################################################################################
def chap0402_04():
    '''
    字典的格式化字符串
    '''
    phonebook = {'Beth': '1234', 'Cecil': '2345', "Alice": "5678"}

    print("chap0402_04 :")
    print("Beth's phone numer = %(Beth)s" % phonebook)
    print("Cecil's phone numer = {Cecil}".format(**phonebook))
    print("Alice's phone numer = {Alice}".format(Alice=phonebook['Alice']))
    print("")



################################################################################
def chap0402_05():
    '''
    原地清除字典中所有的项
    '''
    print("chap0402_05 :")

    d = {}
    d['name'] = 'Gumby'
    d['age'] = 34

    print("清除前字典的值 = {0}，对象ID = {1}".format(d, id(d)))
    returned_valude = d.clear()
    print("清除后字典的值 = {0}，对象ID = {1}，返回值 = {2}".format(d, id(d), returned_valude))
    print("")

################################################################################
def chap0402_06():
    
    x = {}
    y = x 
    x['key'] = 'val'

    print("chap0402_06 :")
    print("初始 x = {0} x_id = {1}, y = {2} y_id = {3}".format(x, id(x), y, id(y)))
    
    x = {}
    print('x={{}}清空后 x = {0} x_id = {1}, y = {2} y_id = {3}'.format(x, id(x), y, id(y)))

    x = y
    print("初始 x = {0} x_id = {1}, y = {2} y_id = {3}".format(x, id(x), y, id(y)))

    x.clear()
    print('x.clear()清空后 x = {0} x_id = {1}, y = {2} y_id = {3}'.format(x, id(x), y, id(y)))

    print("")

################################################################################
def chap0402_07():
    '''
    字典浅copy，副本调用remove()等原地修改值的方法后，源副本都将发生变化
    '''
    x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
    y = x.copy()

    print("chap0402_07 :")
    print('x.copy()后 x = {0} x_id = {1}, y = {2} y_id = {3}'.format(x, id(x), y, id(y)))
 
    y['username'] = '123qwe'
    y['machines'].remove('bar')
    print('y[“machines”].remove()原地修改后 x = {0} x_id = {1}, y = {2} y_id = {3}'.format(x, id(x), y, id(y)))
    print("")


################################################################################
def chap0402_08():
    '''
    字典深deepcopy，调用remove()等原地修改值的方法后，只变化修改的那个字典
    '''
    from copy import deepcopy
    d = {}
    d['names'] = ['Alfred', 'Bertrand']
    c = d.copy()
    dc = deepcopy(d)

    print("chap0402_08 :")
    print('原地修改值前 : d = {0} d_id = {1}'.format(d, id(d)))
    print('原地修改值前 : c = {0} c_id = {1}'.format(c, id(c)))
    print('原地修改值前 : dc = {0} dc_id = {1}'.format(dc, id(dc)))

    d['names'].append('Clive')
    print('原地修改值后 : d = {0} d_id = {1}'.format(d, id(d)))
    print('原地修改值后 : c = {0} c_id = {1}'.format(c, id(c)))
    print('原地修改值后 : dc = {0} dc_id = {1}'.format(dc, id(dc)))
    print("")

################################################################################
def chap0402_09():
    '''
    使用指定的键创建新字典
    '''
    d1 = {}.fromkeys(['name', 'age'])
    d11 = {}.fromkeys(['name', 'age'], 'unknown')

    d2 = dict.fromkeys(['name', 'age'])
    d22 = dict.fromkeys(['name', 'age'], 'unknown')

    print("chap0402_09 :")
    print("通过{{}}.fromkeys创建一个新字典 : ", d1)
    print("通过{{}}.fromkeys创建一个指定默认值的新字典 : ", d11)
    print("通过dict.fromkeys创建一个新字典 : ", d2)
    print("通过dict.fromkeys创建一个指定默认值的新字典 : ", d22)
    print("")

################################################################################
def chap0402_10():
    '''
    通过get获取字典的键值
    '''
    d = {}
    ditem_v1 = d.get('name')
    ditem_v2 = d.get('name', 'N/A')

    print("chap0402_10 :")
    print('get()不指定默认值获得没有的key的值 ditem_v1 = {0}'.format(ditem_v1))
    print('get()指定默认值获得没有的key的值 ditem_v2 = {0}'.format(ditem_v2))
    print("")


################################################################################
def chap0402_11():
    '''
    items方法将字典转成列表
    '''
    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
    it = d.items()

    print("chap0402_11 :")
    print('原始字典 d = {0}'.format(d))
    print('d.items() = {0}, type = {1}'.format(it, type(it)))
    print("")


################################################################################
def chap0402_12():
    '''
    keys获取字典中键，返回迭代器
    '''
    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
    it = d.keys()

    print("chap0402_12 :")
    print('原始字典 d = {0}'.format(d))
    print('d.keys() = {0}, type = {1}'.format(it, type(it)))
    print('')

################################################################################
def chap0402_13():
    '''
    pop方法的使用，迭代中要注意pop改变了原始字典的长度大小
    '''
    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
    l_ks = list(d.keys())

    print("chap0402_13 :")
    print('原始字典 d = {0}'.format(d))
    print('list(d.keys()) = {0}, type = {1}'.format(l_ks, type(l_ks)))
    for k in l_ks:
        d.pop(k)
    
    print('迭代pop()完成后的 d = {0}, type = {1}'.format(d, type(d)))
    print("")


################################################################################
def chap0402_14():
    '''
    popitem 随机pop，无需指定key
    '''
    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
    print("chap0402_14 :")
    print('原始字典 d = {0}'.format(d))
    dlen = len(d)
    for _ in range(dlen):
        d.popitem()

    print('迭代popitem()完成后的 d = {0}, type = {1}'.format(d, type(d)))
    print("")
    

################################################################################
def chap0402_15():
    '''
    setdefault 字典中已有的键保持原值
    '''

    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
    print("chap0402_15 :")
    print('原始字典 d = {0}'.format(d))   

    d.setdefault('title', 'title new val')
    print('setdefault 已有的title键后 d = {0}'.format(d))

    d.setdefault('title2')
    print('setdefault 没有的title2键后 d = {0}'.format(d))
    print("")    

  
################################################################################
def chap0402_16():
    '''
    update方法, 支持所有用于dict()的参数类型
    '''
    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
    print("chap0402_16 :")
    print('原始字典 d = {0}'.format(d))   

    ud_tile = {'title':'Python Language Website'}
    d.update(ud_tile)
    print('update title 后的字典 d = {0}'.format(d))

    ud_url = [('url', 'www.google.com')]
    d.update(ud_url)
    print('update url 后的字典 d = {0}'.format(d))
    print("")  

################################################################################
def chap0402_17():
    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}


    it_vals = d.values()

    print("chap0402_17 :")
    print('原始字典 d = {0}'.format(d))   
    print('d.keys() = {0}, type = {1}'.format(it_vals, type(it_vals)))
    print('')

# 第2章 原生例题
################################################################################
def chap04_01(name=None, key=None):
    '''
    字典示例
    name = 'Alice' | 'Beth' | 'Cecil'
    key = 'phone' | 'addr'
    '''
    people = {
        'Alice' : {
            'phone' : '2341',
            'addr' : 'Foo drive 23'
        },
        'Beth' : {
            'phone' : '9102',
            'addr' : 'Bar street 42'
        },
        'Cecil' : {
            'phone' : '3158',
            'addr' : 'Baz avenue 90'
        }
    }

    labels = {
        'phone' : 'phone number',
        'addr' : 'address'
    }
    if name is None:
        name = input("Name : ")
    
    if key is None:    
        request = input('Phone number (p) or address (a) : ')
        if request == 'p':
            key = 'phone'
        if request == 'a':
            key = 'addr'   

    print("chap04_01 :")
    if name in people:
        print("%s's %s = %s"%(name, labels[key], people[name][key])) 
    
    print("")


################################################################################
def chap04_02(name=None, key=None):
    '''
    使用get增加程序的灵活性
    '''

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

    if name is None:
        name = input('Name: ')

    if key is None:    
        request = input('Phone number (p) or address (a)')
        key = request
        if request == 'p': key = 'phone'
        if request == 'a': key = 'addr'


    person = people.get(name, {})
    label = labels.get(key, key)
    result = person.get(key, 'not available')

    print("chap04_02 :")
    print("%s's %s is %s" % (name, label, result))
    print("")

################################################################################
def main_chap04():

    chap0402_01()

    chap0402_02()

    chap0402_02(((('name', 'Gumby'), ('age', 33))))
    
    chap0402_03()

    chap0402_04()

    chap0402_05()

    chap0402_06()
    
    chap0402_07()

    chap0402_08()

    chap0402_09()

    chap0402_10()
    
    chap0402_11()

    chap0402_12()

    chap0402_13()

    chap0402_14()

    chap0402_15()

    chap0402_16()

    chap0402_17()

    ################################################################################
    chap04_01('Beth', 'phone')

    chap04_02('Beth', 'phone')

    chap04_02('Beth', 'aphone')

################################################################################
if __name__ == '__main__':
    main_chap04()
