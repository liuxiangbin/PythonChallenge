#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 16
        let me get this straight.
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function

from PIL import Image

def get_straight(img):
    width,height = img.size
    pink = 195
    res_img = img.copy()
    for y in range(height):
        line = [img.getpixel((x,y)) for x in range(width)]
        index = line.index(pink)
        line = line[index:] + line[:index]
        for i,val in enumerate(line):
            res_img.putpixel((i,y),val)
    
    return res_img

if __name__ == "__main__":
    img_path = "../data/mozart.gif"
    img = Image.open(img_path)
    get_straight(img).show()