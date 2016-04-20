#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 2
        find alpha character.
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function
import urllib

def find_alpha(str):
    """
        find character in str.
    """
    res = [c for c in str if c.isalpha()]
    return ''.join(res)

if __name__ == "__main__":
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    request = urllib.urlopen(url)
    str = request.read()
    print(find_alpha(str[str.rindex('<!--'):]))