#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*****************************************************************************************
# ぐるなびWebサービスの応援口コミAPIを実行しハンバーグの口コミを取得しパースするプログラム
# 注意：アクセスキーはユーザ登録後に発行されるキーを指定してください。
#*****************************************************************************************
import sys
import urllib
import json
 
####
# 変数の型が文字列かどうかチェック
####
def is_str( data = None ) :
  if isinstance( data, str ) or isinstance( data, unicode ) :
    return True
  else :
    return False

def generate_html(html_txt):
    message = """
    <!DOCTYPE html>
    <html lang="ja">
      <head><meta charset="UTF-8"></head>
      <body>
        %s
      </body>
    </html>
    """
    return message % html_txt


def generate_txt():
    template = """
    店舗名:<a href="{0}">{1}</a><br/>
    コメント：{2}<br/>
    <img src="{3}"><br/><br/>
    """
    content = ''
    #photo = data["response"]["{0}".format(i)]["photo"]
    content += template.format(photo["shop_url"].encode(encoding), photo["shop_name"].encode(encoding),photo["comment"].encode(encoding), photo["image_url"]["url_320"].encode(encoding))
    return content


####
# 初期値設定
####
# APIアクセスキー
keyid     = "**************************************"
# エンドポイントURL
url       = "http://api.gnavi.co.jp/PhotoSearchAPI/20150630/"
# メニュー
#menu_name = u"ハンバーグ"
menu_name = "coffee"
#文字コード
encoding = 'utf-8'
#ヒット件数
hit_per_page = 3
 
####
# APIアクセス
####
# URLに続けて入れるパラメータを組立
query = [
  ( "format",    "json"    ),
  ( "keyid",     keyid     ),
  ( "menu_name", menu_name.encode(encoding) ),
  ( "hit_per_page", hit_per_page ),
]
# URL生成
url += "?{0}".format( urllib.urlencode( query ) )
# API実行
try :
  result = urllib.urlopen( url ).read()
except ValueError :
  print u"APIアクセスに失敗しました。"
  sys.exit()
 
####
# 取得した結果を解析
####
data = json.loads( result )
 
# エラーの場合
if "error" in data :
  if "message" in data :
    print u"{0}".format( data["message"] )
  else :
    print u"データ取得に失敗しました。"
  sys.exit()
 
# ヒット件数取得
total_hit_count = None
if "total_hit_count" in data["response"] :
  total_hit_count = data["response"]["total_hit_count"]
 
#ページごとの件数を取得
hit_per_page = None
if "hit_per_page" in data["response"] :
  hit_per_page = data["response"]["hit_per_page"]
 
# ヒット件数が0以下、または、ヒット件数がなかったら終了
if total_hit_count is None or total_hit_count <= 0 or hit_per_page is None or hit_per_page <= 0 :
  print u"指定した内容ではヒットしませんでした。"
  sys.exit()
 
# ヒット件数表示
print "{0}件ヒットしました。".format( total_hit_count )
print "----"
 
# 出力件数
disp_count = 0

html_text=""

# 応援口コミデータ取得
for i in range( hit_per_page ) :
  photo = data["response"]["{0}".format(i)]["photo"]
  line                 = []
  id                   = ""
  name                 = ""
  mname                = ""
  comment              = ""
 
  # 店舗番号
  if "shop_id" in photo and is_str( photo["shop_id"] ) :
    id = photo["shop_id"]
  line.append( id )
 
  # 店舗名
  if "shop_name" in photo and is_str( photo["shop_name"] ) :
    name = photo["shop_name"]
  line.append( name )
 
  # メニュー名
  if "menu_name" in photo and is_str( photo["menu_name"] ) :
    mname = photo["menu_name"]
  line.append( mname )
 
  # コメント
  if "comment" in photo and is_str( photo["comment"] ) :
    comment = photo["comment"]
  line.append( comment )
 
  # タブ区切りで出力
  #print " \t".join( line )
  html_text+=generate_txt()
  disp_count += 1


with open("test.html","w") as f:
  f.write(generate_html(html_text))
import webbrowser
webbrowser.open_new_tab("test.html")

# 出力件数を表示して終了
print "----"
print "{0}件出力しました。".format( disp_count )
sys.exit()
