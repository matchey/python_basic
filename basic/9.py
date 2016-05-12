# -*- coding: utf-8 -*-

#import os
#os.getcwd()

#9. 各行を２コラム目、１コラム目の優先順位で辞書の逆順にソートして出力せよ
def rsort_str(input_file):
    with open(input_file) as ifile:
        lines = sorted([line.split('\t') for line in ifile], key=lambda x:x[0],reverse=True)
    for line in sorted(lines,key=lambda x:x[1],reverse=True):
        print '\t'.join(line),

if __name__=='__main__':
    filename="address.txt"
    rsort_str(filename)

