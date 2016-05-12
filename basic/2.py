# -*- coding: utf-8 -*-

#import os
#os.getcwd()

#2.タブ1文字につきスペース1文字に置換せよ
def pat_replace(stxt,rtxt,file):
    try:
        ofile = open('tmp','w')
        ifile = open(file)
    except IOError:
        print '"%s" cannot be opened.' % file
    else:
        lines=ifile.readlines()
        ifile.close()
        ifile=open(file,'w')
        for line in lines:
            a = line.replace(stxt,rtxt)
            ifile.write(a)
            ofile.write(line)
    finally:
        ofile.close()
        ifile.close()

if __name__=='__main__':
    filename="address.txt"
    txt_old="\t"
    txt_new=" "
    pat_replace(txt_old,txt_new,filename)

