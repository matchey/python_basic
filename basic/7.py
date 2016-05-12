# -*- coding: utf-8 -*-
from collections import Counter

#import os
#os.getcwd()

#7. １コラム目の文字列を集計して表示せよ(文字列/カウントを表示）
def cnt_str(input_file):
    try:
        ifile = open(input_file)
    except IOError:
        print '"%s" cannot be opened.' % input_file
    else:
        c=Counter()
        for line in ifile:
            cols=line.split()
            c[cols[0]]+=1
        for name,count in c.items():
            print '(%s/%d)' % (name,count)
    finally:
        ifile.close()

if __name__=='__main__':
    filename="address.txt"
    cnt_str(filename)

