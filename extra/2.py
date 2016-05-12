#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*****************************************************************************************
#2. コマンドライン引数から受け取った検索キーワードが日本語かどうか判定し、
#   それにより利用する検索APIをそれぞれレストラン検索API/多言語版レストラン検索APIで切り替えよ。
#   なお、条件により対応するAPIの数は今後増えていくということを考慮した設計にすること
#*****************************************************************************************
import sys
import urllib
import json
 
# コマンドライン引数からキーワードをもらう
if len(sys.argv) != 2:
    print("Usege: python 2.py keyword")
    sys.exit(0)
else:
    try:
        freeword=sys.argv[1]
        freeword.encode('ascii')
        import gnavi_frgn_show
    except UnicodeDecodeError:
        import gnavi_jp_show

