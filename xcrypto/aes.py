#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################################
import sys


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


#########################################################################################
def AES_TEST():
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
    AES_TEST()
