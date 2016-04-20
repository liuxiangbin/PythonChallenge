#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 1
        character conversion.
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function

def decode_use_map(str):
    '''
        k --> m
        o --> q
        e --> g
        
        char c --> char c+2
    '''
    res = [chr(97+(ord(c)-97+2)%26) if c.isalpha() else c for c in str]
    return ''.join(res)

def decode_use_maketrans(str):
    '''
        k --> m
        o --> q
        e --> g
    
        char c --> char c+2
    ''' 
    import string 
    
    intab = "abcdefghijklmnopqrstuvwxyz"
    outtab = "cdefghijklmnopqrstuvwxyzab"
    trans = string.maketrans(intab,outtab)
    
    return str.translate(trans)


if __name__ == "__main__":
    str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.\
    bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. \
    sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    
    print(decode_use_map(str))
    print(decode_use_map("map"))
    
    print(decode_use_maketrans(str))
    print(decode_use_maketrans("map"))