#!/usr/bin/env python 
# -*- coding:UTF-8 -*-

'''
    Python challenge: level 15
        whom?
        Find 1**6 year whose first day is Thursday.
        he ain't the youngest, he is the second    => 1756
        
        buy flowers for tomorrow =>1756-1-27 Mozart诞辰.
        
    @author: DTree
    @license: GNU General Public License 2.0 or later
    @contact: mycodekingdom@gmail.com
'''

from __future__ import print_function

import datetime

if __name__ == "__main__":
    for year in xrange(1996,1006,-20):
        if datetime.datetime(year,1,1).weekday() == 3:  #Thursday
            print(year)