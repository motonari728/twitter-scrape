from os import read
import re

path = 'data/ayanami.txt'

with open(path) as f:
    text = f.read()
    # text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'(https?)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)', '', text, flags=re.MULTILINE)
    
save_path = 'data/ayanami_withoutURL.txt'
with open(save_path, mode='x') as f:
    f.write(text)
