#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 3
       One small letter, surrounded by EXACTLY three big bodyguards 
       on each of its sides.
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function 
import urllib
import re

def find_pattern(text):
    """
        find all string which matches pattern `[^A-Z][A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]`.
    """
    pattern = re.compile(r"[^A-Z][A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]")
    return pattern.findall(text)


if __name__ == "__main__":
    url = "http://www.pythonchallenge.com/pc/def/equality.html"
    request = urllib.urlopen(url)
    text = request.read()
    text = text[text.rindex('<!--'):]
    print(''.join(find_pattern(text)))
    