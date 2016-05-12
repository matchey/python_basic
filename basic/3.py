# -*- coding: utf-8 -*-

#import os
#os.getcwd()

#3. 各行の１列目だけを抜き出したものをcol1.txtに、２列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ
def col_divide(file):
    try:
        o1file = open('col1.txt','w')
        o2file = open('col2.txt','w')
        ifile = open(file)
    except IOError:
        print '"%s" cannot be opened.' % file
    else:
        for line in ifile:
            dvided=line.split(' ')
            o1file.write(dvided[0]+'\n')
            o2file.write(dvided[1])
    finally:
        o1file.close()
        o2file.close()
        ifile.close()

if __name__=='__main__':
    filename="address.txt"
    col_divide(filename)

