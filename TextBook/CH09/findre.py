
import os
import sys
import re

if len(sys.argv) < 2:
    sys.exit('使い方：python findre.py 正規表現パターン')

pattern = re.compile(sys.argv[1])

for filename in os.listdir('./'):
    if not filename.lower().endswith('.txt'):
        continue
      txt_file = open(filename, 'r', encoding='utf-8')
    for line in txt_file:
        mo = pattern.search(line)
        if mo:
            print(filename, ':',  line, end='')
    txt_file.close()

