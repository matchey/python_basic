#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*****************************************************************************************
#4. 応援APIを利用し、各店舗の応援を取得せよ。取得するのは上位3件の店舗分のみで構わないが、
#   この指定が今後変えられるよう考慮すること。なお、取得処理は並列で実行すること（asyncioを使用）。
#*****************************************************************************************
import sys
import urllib.request, urllib.parse, urllib.error
import json
import asyncio

####
# 変数の型が文字列かどうかチェック
####
def is_str( data = None ) :
  if isinstance( data, str ) or isinstance( data, str ) :
    return True
  else :
    return False

async def get_data(url,menu_name,loop):
####
# APIアクセス
####
# URLに続けて入れるパラメータを組立
    query = [
      ( "format",    "json"    ),
      ( "keyid",     keyid     ),
      ( "hit_per_page", 3 ),
      ( "menu_name", menu_name )
    ]
# URL生成
    url += "?{0}".format( urllib.parse.urlencode( query ) )
# API実行
    try :
      result = urllib.request.urlopen( url ).read().decode('utf8')
    except ValueError :
      print("APIアクセスに失敗しました。")
      sys.exit()
####
# 取得した結果を解析
####
    data = json.loads(result)
    show_result(data)


def show_result(data):
# エラーの場合
    if "error" in data :
      if "message" in data :
        print("{0}".format( data["message"] ))
      else :
        print("データ取得に失敗しました。")
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
      print("指定した内容ではヒットしませんでした。")
      sys.exit()
     
# ヒット件数表示
    print("{0}件ヒットしました。".format( total_hit_count ))
    print("----")
     
# 出力件数
    disp_count = 0
     
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
      print("\t".join( line ))
      disp_count += 1
     
# 出力件数を表示して終了
    print("----")
    print("{0}件出力しました。\n\n".format( disp_count ))


####
# 初期値設定
####
# APIアクセスキー
keyid     = "************************************"
# エンドポイントURL
url       = "http://api.gnavi.co.jp/PhotoSearchAPI/20150630/"
#文字コード
encoding = 'utf-8'
 
# メニュー
menu_name=["coffee","ラーメン","天ぷら"]


loop=asyncio.get_event_loop()

loop.run_until_complete(get_data(url,menu_name[0],loop))
loop.run_until_complete(get_data(url,menu_name[1],loop))
loop.run_until_complete(get_data(url,menu_name[2],loop))


    
sys.exit()

