#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 10
        Look-and-say sequence(外观数列).
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function


def next_num(seq):
    """
        compute look-and-say number of num.
    """
    if not seq:
        return ""
    
    res = ""
    start,count = seq[0],1
    for i in xrange(1,len(seq)):
        if seq[i] == start:
            count += 1
        else:
            res += str(count)+ str(start)
            start,count = seq[i],1
        i += 1
        
    res += str(count) + str(start)
        
    return res

if __name__ == "__main__":
    seq = "1"
    i = 0
    while i < 30:
        print(seq)
        seq = next_num(seq)
        i += 1
        
    print(len(seq))      