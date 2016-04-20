#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 7
        
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function

import Image

if __name__ == "__main__":
    url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
    img = Image.open(url)
    
    print(img)