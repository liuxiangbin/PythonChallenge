#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 11
        odd even.
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function

from PIL import Image

if __name__ == "__main__":
    img_url = "../data/cave.jpg"
    img = Image.open(img_url)
    width,height = img.size
    odd = even = Image.new(img.mode, (width/2,height/2), (0,255,0,0))
    
    for x in xrange(width):
        for y in xrange(height):
            if x%2==0 and y%2==0:
                even.putpixel((x/2,y/2), img.getpixel((x,y)))
            elif x%2 ==1 and y%2==0:
                odd.putpixel(((x-1)/2,y/2), img.getpixel((x,y)))
            elif x%2==0 and y%2==1:
                even.putpixel((x/2,(y-1)/2),img.getpixel((x,y)))
            else:
                odd.putpixel(((x-1)/2,(y-1)/2), img.getpixel((x,y)))
    
    odd.show()
    even.show()