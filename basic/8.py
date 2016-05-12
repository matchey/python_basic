# -*- coding: utf-8 -*-

#import os
#os.getcwd()

#8. 各行を２コラム目の辞書順にソートして出力せよ
def sort_str(input_file):
    with open(input_file) as ifile:
        lines = sorted([line.split('\t') for line in ifile], key=lambda x:x[1])
    for line in lines:
        print '\t'.join(line),

if __name__=='__main__':
    filename="address.txt"
    sort_str(filename)

