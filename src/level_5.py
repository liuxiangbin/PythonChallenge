#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 5
        peak hell sounds familiar ? Pickle
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function
import urllib
import time

try:
    import cPickle as pickle
except ImportError:
    import pickle

if __name__ == "__main__":
    start = time.time()
    
    url = "http://www.pythonchallenge.com/pc/def/banner.p"
    req = urllib.urlopen(url)
    result = pickle.load(req)
    for item in result:
        print(''.join([elem[0]*elem[1] for elem in item]))
        
    print("Total time is : %.3f seconds"%(time.time()-start))