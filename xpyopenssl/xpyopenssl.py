#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==============================================================================
#
# Author            : iaiting
#
# Contact           : iaiting@aliyun.com
#
# Generate Data     : 2018-03-22
#
# Copyright         : 本文件隶属iaiting，欢迎转载无须知会
#
# Desciption        : cryptography库的学习
#
# ==============================================================================
#
# 字符画生成网址   : http://patorjk.com/software/taag
#
# ==============================================================================

from cryptography.fernet import Fernet


def welcomeinfo_display():
    info='''
             __                     __                           __                          __
 _    _____ / /______  __ _  ___   / /____    __________ _____  / /____  ___ ________ ____  / /  __ __
| |/|/ / -_) / __/ _ \/  ' \/ -_) / __/ _ \  / __/ __/ // / _ \/ __/ _ \/ _ `/ __/ _ `/ _ \/ _ \/ // /
|__,__/\__/_/\__/\___/_/_/_/\__/  \__/\___/  \__/_/  \_, / .__/\__/\___/\_, /_/  \_,_/ .__/_//_/\_, /
                                                    /___/_/            /___/        /_/        /___/
'''
    print(info)

def fernet_test():
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(b"A really secret message. Not for prying eyes.")
    print(token)
    p=f.decrypt(token)
    print(p)

# ==============================================================================
def xcryptography():
    welcomeinfo_display()
    fernet_test()

# ==============================================================================
if __name__ == '__main__':
    xcryptography()
