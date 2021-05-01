import os
import twint


c = twint.Config()
# c.Limit = 10


# ユーザー名の指定
# c.Username = "tarouo_mavs" #サンプル
c.Username = "reflask" #サンプル
# c.Username = "ayanami_rei_T"

# リプライを除こうとしたが、うまく行かず
# c.Search = "-filter:replies"


# Outputファイル
# c.Output = "tweets.csv"
c.Output = "tweets.json"

# フォーマット指定はエラー吐く
# c.Format = "tweet"
# c.Format = "ID {id} | Username {username}"


# ファイルフォーマット指定
# c.Store_csv = True
c.Store_json = True


# 前回のスクレイピングの結果を削除
os.remove("tweets.json")

# スクレイピング
# retweetは含まず、replyは含む
twint.run.Search(c)






