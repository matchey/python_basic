#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*****************************************************************************************
#
#1. コマンドライン引数から検索キーワードを受け取り、ぐるなびAPIにアクセスし検索結果(店舗名)を出力せよ。受け取るデータ型はJSON形式にすること
#
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
 
####
# 初期値設定
####
# APIアクセスキー
keyid     = "**********************************"
# エンドポイントURL
url       = "http://api.gnavi.co.jp/RestSearchAPI/20150630/"
# コマンドライン引数からキーワードをもらう
if len(sys.argv)==2:
    freeword=sys.argv[1]
else:
    print("Usege: python 1.py keyword")
    sys.exit(0)

####
# APIアクセス
####
# URLに続けて入れるパラメータを組立
query = [
  ( "format",    "json"    ),
  ( "keyid",     keyid     ),
  ( "freeword", freeword   )
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
if "total_hit_count" in data :
  total_hit_count = data["total_hit_count"]
 
# ヒット件数が0以下、または、ヒット件数がなかったら終了
if total_hit_count is None or total_hit_count <= 0 :
  print u"指定した内容ではヒットしませんでした。"
  sys.exit()
 
# レストランデータがなかったら終了
if not "rest" in data :
  print u"レストランデータが見つからなかったため終了します。"
  sys.exit()
 
# ヒット件数表示
print "{0}件ヒットしました。".format( total_hit_count )
print "----"
 
# 出力件数
disp_count = 0
 
# レストランデータ取得
for rest in data["rest"] :
  line                 = []
  id                   = ""
  name                 = ""
  access_line          = ""
  access_station       = ""
  access_walk          = ""
  code_category_name_s = []
  # 店舗番号
  if "id" in rest and is_str( rest["id"] ) :
    id = rest["id"]
  line.append( id )
  # 店舗名
  if "name" in rest and is_str( rest["name"] ) :
    name = u"{0}".format( rest["name"] )
  line.append( name )
  if "access" in rest :
    access = rest["access"]
    # 最寄の路線
    if "line" in access and is_str( access["line"] ) :
      access_line = u"{0}".format( access["line"] )
    # 最寄の駅
    if "station" in access and is_str( access["station"] ) :
      access_station = u"{0}".format( access["station"] )
    # 最寄駅から店までの時間
    if "walk"    in access and is_str( access["walk"] ) :
      access_walk = u"{0}分".format( access["walk"] )
  line.extend( [ access_line, access_station, access_walk ] )
  # 店舗の小業態
  if "code" in rest and "category_name_s" in rest["code"] :
    for category_name_s in rest["code"]["category_name_s"] :
      if is_str( category_name_s ) :
        code_category_name_s.append( u"{0}".format( category_name_s ) )
  line.extend( code_category_name_s )
  # タブ区切りで出力
  print "\t".join( line )
  disp_count += 1
 
# 出力件数を表示して終了
print "----"
print u"{0}件出力しました。".format( disp_count )
sys.exit()
