# -*- coding: utf-8 -*-

import sys
#os.getcwd()

#5.自然数Nをコマンドライン引数にとり、入力のうち先頭のN行だけ出力せよ
def top_output(file):
    try:
        ifile = open(file)
        row=int(sys.argv[1])
    except IndexError:
        print 'Usage: %s N(natural number)' % sys.argv[0]
    except IOError:
        print '"%s" cannot be opened.' % file
    else:
        lines=ifile.readlines()
        if row>len(lines):
            row=len(lines)
        for i in range(row):
            print lines[i],
    finally:
        ifile.close()

if __name__=='__main__':
    filename="address.txt"
    top_output(filename)

