#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 14
        walk around.
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function

from PIL import Image

def spiral(new_img,x_start,x_end,y_start,y_end,old_img,x):
    """
        Transform old_img to new_img in spiral order.
        
        up->down, left->right, down->up, right->left.
    """
    if x_start > x_end or y_start > y_end:
        return
    
    #up->down
    for row in range(x_start,x_end+1):
        new_img.putpixel((row,y_start),old_img.getpixel((x,0)))
        x += 1
    #left-> right
    for col in range(y_start+1,y_end+1):
        new_img.putpixel((x_end,col),old_img.getpixel((x,0)))
        x += 1
    #down->up
    for row in range(x_end-1,x_start-1,-1):
        new_img.putpixel((row,y_end),old_img.getpixel((x,0)))
        x += 1
    #right->left
    for col in range(y_end-1,y_start,-1):
        new_img.putpixel((x_start,col),old_img.getpixel((x,0)))
        x += 1
    #recursive
    spiral(new_img,x_start+1,x_end-1,y_start+1,y_end-1,old_img,x)
    

if __name__ == "__main__":
    img_path = "../data/wire.png"
    img = Image.open(img_path)
    print(img.size)
    
    res_img = Image.new(img.mode,(100,100),(0,255,0,0))
    spiral(res_img,0,99,0,99,img,0)
    res_img.show()
