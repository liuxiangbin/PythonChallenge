#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 13
        phone that evil.
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function

import xmlrpclib

if __name__ == "__main__":
    url = "http://www.pythonchallenge.com/pc/phonebook.php"
    
    pb = xmlrpclib.ServerProxy(url)
    
    print(pb.system.listMethods())
    
    # *Bert* comes from 'http://www.pythonchallenge.com/pc/return/evil4.jpg'
    print(pb.phone('Bert'))