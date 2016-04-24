#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 17
        eat? About cookies.
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function

import urllib2
import cookielib
import urllib
import bz2

def get_opener(url,username,password):
    """
        Get a urllib2 opener for url which needs auth,
        return the opener and cookiejar.
    """
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password('inflate',url,username,password)
    jar = cookielib.CookieJar()
    cookie_handler = urllib2.HTTPCookieProcessor(jar)
    opener = urllib2.build_opener(auth_handler,cookie_handler)
    
    return (opener,jar)

def get_cookies_msg(opener,jar):
    """
        Get the message from cookies.
    """
    message = ""
    num = "12345"
    while True:   
        text = opener.open("http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s"%(num)).read()
        message += list(jar)[0].value
        try:
            num = text[text.index("and the next busynothing is")+28:]
        except ValueError:
            break
    
    return message
    

if __name__ == "__main__":
    url = "http://www.pythonchallenge.com/pc/return/romance.html"
    opener,jar = get_opener(url, 'huge', 'file')
    opener.open(url)
     
    print(list(jar))
    
    message = get_cookies_msg(opener,jar)
    print(message)
        
    message = urllib.unquote_plus(message)
    #bz2 decompress the message
    print(bz2.decompress(message))
    
    #go to level 13, get Leopold's phone number.
    
    url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
    list(jar)[0].value = "the flowers are on their way"
    print(opener.open(url).read())