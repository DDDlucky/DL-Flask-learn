# -*- coding: utf-8 -*-

from flickrapi import FlickrAPI #FlikcrAPIクライアントのクラス定義
from urllib.request import urlretrieve #コマンドラインからhttp通信をする関数
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import os, time, sys #Pythonからシステムにアクセスする関数, タイマー関数

key = "fae8b8e5d6a8102c7527b8bb2cf2e67c"
secret = "9969c774ad3434e1"
wait_time = 1 #リクエストを発行するインターバル

animalname = sys.argv[1] #コマンドラインで2番目の引数を取得
savedir = "./" + animalname #引数で与えた単語名でフォルダーを作成

flickr = FlickrAPI(key, secret, format='parsed-json')

result = flickr.photos.search(
    text = animalname, #検索ワード
    per_page = 400, #検索数上限
    media = 'photos', #データタイプ
    sort = 'relevance', #結果表示順, 最新から
    safe_search = 1, #子どもに不敵な画像を除外
    extras = 'url_q, licence' #オプション。データURL, ライセンスタイプ
)

photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q'] #photoオブジェクトからダウンロードURLを取得
    filepath = savedir + '/' + photo['id'] + '.jpg' #ファイル名をフルパスで生成
    if os.path.exists(filepath): continue #ファイルがあれば次へ
    urlretrieve(url_q,filepath) #ファイルダウンロードを実行
    time.sleep(wait_time) #サーバー負荷を考慮して1秒あける

