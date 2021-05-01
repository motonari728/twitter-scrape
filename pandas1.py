import pandas as pd



df = pd.read_json('tweets.json', lines = True)
# print(df.columns)
print("列名, 型")
print(df.dtypes)

print("行数")
print(len(df.index))


# replyを除外するため、reply_toが空白かどうか調べる
is_empty = lambda x: len(x) == 0
df = df[df['reply_to'].apply(is_empty)]

df.to_csv('data/tweets.txt', columns=['tweet'], header=False, index=False)


