#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 4
        urllib may help. DON’T TRY ALL NOTHINGS, since it will never
        end. 400 times is more than enough.
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function
import urllib

if __name__ == "__main__":
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    num = "12345"
    i = 0
    while i < 400:
        request = urllib.urlopen(url+num)
        text = request.read()
        print(text)
        if text.find(".html") != -1:
            break
        
        try:
            num = text[text.index("and the next nothing is")+24:]
        except ValueError:
            num = str(int(num)/2)

        i += 1
    
    print(text)