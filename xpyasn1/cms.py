#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################################
import sys

from pyasn1.codec.der.encoder import encode
from pyasn1.codec.native.decoder import decode
from pyasn1.codec.native.encoder import encode
from pyasn1.type import univ
from pyasn1.type import univ, namedtype, tag


#########################################################################################
class Record(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('id', univ.Integer()),
        namedtype.OptionalNamedType(
            'room',
            univ.Integer().subtype(
                implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple,
                                    0))),
        namedtype.DefaultedNamedType(
            'house',
            univ.Integer(0).subtype(
                implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple,
                                    1))))


#########################################################################################
def cms():
    print("Enter Function:", sys._getframe().f_code.co_name)
    internetId = univ.ObjectIdentifier((1, 3, 6, 1))
    print(internetId)
    record = Record()
    record['id'] = 123
    print(record.prettyPrint())
    record[1] = 321
    print(record.prettyPrint())

    record.setDefaultComponents()
    print(record.prettyPrint())


#########################################################################################
def cms_test():
    print("Enter Function:", sys._getframe().f_code.co_name)
    cms()


#########################################################################################
if __name__ == '__main__':
    cms_test()
    print()
