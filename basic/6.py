# -*- coding: utf-8 -*-

import sys
#os.getcwd()

#6. 自然数Nをコマンドライン引数にとり、入力のうち末尾のN行だけ出力せよ
def bottom_output(file):
    try:
        ifile = open(file)
        row=int(sys.argv[1])
    except IndexError:
        print 'Usage: %s N(natural number)' % sys.argv[0]
    except IOError:
        print '"%s" cannot be opened.' % file
    else:
        lines=ifile.readlines()
        row_num=len(lines)
        if row>row_num:
            row=row_num
        for i in range(row_num,row_num-row,-1):
            print lines[i-1],
    finally:
        ifile.close()

if __name__=='__main__':
    filename="address.txt"
    bottom_output(filename)

