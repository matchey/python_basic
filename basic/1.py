# -*- coding: utf-8 -*-

#import os
#os.getcwd()

#1.ファイルの行数をカウントせよ
lin_num=sum(1 for line in open("address.txt","r"))

if __name__=='__main__':
    print lin_num

