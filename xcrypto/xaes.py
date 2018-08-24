#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################################
# PyCtypto 已经不再维护了，迁移到 PyCryptodome
import sys
from Crypto.Random import get_random_bytes
from base64 import b64encode

import base64

#########################################################################################
#
# AES 加密相关函数
#
#########################################################################################

def AES_Encrypt(key, iv, plainIn):
    cipherOut = plainIn
    return cipherOut


#########################################################################################
#
# AES 解密相关函数
#
#########################################################################################
def AES_Decrypt(key, iv, cipherIn):
    plainOut = cipherIn
    return plainOut



class CXAES(object):

    @staticmethod
    def gen_key(size):
        v1 = get_random_bytes(size)
        v2 = b64encode(v1)
        print(v1)
        print(v2)
        base64.b16encod
        e()
        return v2




#########################################################################################
def XAES_TEST():
    print("Enter Function:", sys._getframe().f_code.co_name)
    key = "1234567890abcdef"
    iv = "fedcba0987654321"
    plainIn = "abc123"
    cipherOut = AES_Encrypt(key, iv, plainIn)
    plainOut = AES_Decrypt(key, iv, cipherOut)

    print("cipher out:", cipherOut)
    print("plain out:", plainOut)


#########################################################################################
if __name__ == '__main__':
    CXAES.gen_key(16)
#    XAES_TEST()
