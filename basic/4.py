# -*- coding: utf-8 -*-

#import os
#os.getcwd()

#4. 3で作ったcol1.txtとcol2.txtを結合し，元のタブ区切りテキストを復元せよ
def combine_col(col1file,col2file,cmb_file):
    try:
        i1file = open(col1file)
        i2file = open(col2file)
        ofile = open(cmb_file,'w')
    except IOError:
        print 'file cannot be opened.'
    else:
        lines2=i2file.readlines()
        for i in range(len(lines2)):
            line1=i1file.readline().replace('\n','\t')
            ofile.write(line1+lines2[i])
    finally:
        i1file.close()
        i2file.close()
        ofile.close()

if __name__=='__main__':
    filename="address.txt"
    divided1="col1.txt"
    divided2="col2.txt"
    combine_col(divided1,divided2,filename)

