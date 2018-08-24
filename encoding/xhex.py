#!/usr/bin/env python3
# -*- coding: utf-8


################################################################################
def hexEncode(b):
    '''
    [IN]	: bytes
    [OUT]	: str
    '''

    return b.hex()


################################################################################
def hexDecode(s):
    '''
    [IN]	: str
    [OUT]	: bytes
    '''

    return bytes.fromhex(s)

################################################################################
class CXHex(object):
    pass

################################################################################
def xhex_test():
    t_b = b'1\x31'
    t_hexstr = hexEncode(t_b)
    print("{0}'s hex string is {1}".format(t_b, t_hexstr))

    t_b = hexDecode(t_hexstr)
    print("{0}'s bytes is {1}".format(t_hexstr,t_b))

################################################################################
if __name__ == "__main__":
    xhex_test()
