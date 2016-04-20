#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 6
        find the zip.
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function

import zipfile
#import sys

if __name__ == "__main__":
    zipFileName = "../data/channel.zip"
    z = zipfile.ZipFile(zipFileName,"r")
    num = "90052"
    
#     f = open("tmp.txt","w")
#     sys.stdout = f        #redirct the stdout to f

    comment = ""
    while True:
        text = z.read(num+".txt")
        print(text)
        info = z.getinfo(num+".txt")
        comment += info.comment
        try: 
            num = text[text.index("Next nothing is")+16:]
            #print(num)
        except ValueError:
            break
    
    print(comment)