#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

################################################################################
#
# RSA 加密相关函数
#
################################################################################
def RSA_Encrypt():
    pass

def RSA_EncryptBytes2Bytes():
    pass

def RSA_EncryptBytes2Hexstr():
    pass

################################################################################
#
# RSA 解密相关函数
#
################################################################################
def RSA_Decrypt():
    pass

def RSA_DecryptBytes2Bytes():
    pass

def RSA_DecryptHexstr2Bytes():
    pass


################################################################################
class CXRSA(object):

    @staticmethod
    def gen_key(bits=2048, format='DER'):

        key = RSA.generate(bits)

        private_key = key.export_key(format)

        public_key = key.publickey().export_key(format)

        #        return private_key.hex(), public_key.hex()
        return private_key, public_key

    @staticmethod
    def encrypt(data, rec_publ_key):
        recipient_key = RSA.import_key(rec_publ_key)
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        return cipher_rsa.encrypt(data)


    @staticmethod
    def decrypt(data, priv_key):
        key = RSA.import_key(priv_key)
        cipher_rsa = PKCS1_OAEP.new(key)
        return cipher_rsa.decrypt(data)


################################################################################

################################################################################
#
# rsa.py testing function
#
################################################################################
def XRSA_TEST():
    # print("Start Testing:", __file__)
    private_key, public_key = CXRSA.gen_key()
    print("私钥 : \n{0}".format(private_key.hex()))
    print("公钥 : \n{0}".format(public_key.hex()))



    secret = b'This Is The Password'
    # encrypt data
    ciphertext = CXRSA.encrypt(secret, public_key)
    print("加密结果 : \n{0}".format(ciphertext.hex()))

    # decrypt data
    plaintext = CXRSA.decrypt(ciphertext, private_key)
    print("解密结果 : \n{0}".format(plaintext))

    # public_key, private_key = CXRSA.gen_key()

################################################################################
if __name__ == '__main__':
    XRSA_TEST()
