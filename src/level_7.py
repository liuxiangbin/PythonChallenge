#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 7
        resolve picture oxygen.png.
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function

from PIL import Image

if __name__ == "__main__":
    img_path = "../data/oxygen.png"
    img = Image.open(img_path)
    
    x_min,x_max = (0,608)
    y_min,y_max = (43,51)
    step = 7
    print(''.join([chr(img.getpixel((x,y_max))[0]) for x in xrange(x_min,x_max,step)]))
    
    nums = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    print(''.join([chr(num) for num in nums]))