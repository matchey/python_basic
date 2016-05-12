# -*- coding: utf-8 -*-
from collections import Counter

#import os
#os.getcwd()

#10. 各行の２コラム目の文字列の出現頻度を求め、出現頻度の高い順に並べよ。ただし、3で作成したプログラムの出力（col2.txt）を読み込むプログラムとして実装せよ 
def sort_cnt(input_file):
    try:
        ifile = open(input_file)
    except IOError:
        print '"%s" cannot be opened.' % input_file
    else:
        c=Counter()
        for line in ifile:
            c[line]+=1
        for name in sorted(c.items(),key=lambda x:x[1],reverse=True):
            print '(%s/%d)' % (name[0].rstrip(),name[1])
    finally:
        ifile.close()

if __name__=='__main__':
    filename="col2.txt"
    sort_cnt(filename)

