#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 12
        dealing evil.
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function


if __name__ == "__main__":
    gfx = "../data/evil2.gfx"
    types = ['jpg','png','gif','png','jpg']
    
    with open(gfx,"rb") as f:
        data = f.read()
        
        for i in range(5):
            img = open("../result/evil_%d.%s"%(i,types[i]),"wb")
            img.write(data[i::5])
            img.close()