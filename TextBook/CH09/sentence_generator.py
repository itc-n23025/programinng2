import sys
import re

if len(sys.argv) < 2:
    sys.exit('Usage: sentence_generator.py src.txt')

src_file = open(sys.argv[1], 'r')
src_data = src_file.read()
src_file.close()

pattern = re.compile(r'(ADJECTIVE|NOUN|VERB|ADVERB)')

while True:

    mo = pattern.search(src_data)
    if not mo:
        break

    print('Enter a', end='')

    if mo.group(1)[0] == 'A':
        print('n', end='')
    repl = input(' ' + mo.group(1).lower() + ': ')

    src_data = src_data.replace(mo.group(1), repl, 1)

print(src_data, end='')

dst_file = open(sys.argv[1] + '.generated.txt', 'w')
dst_file.write(src_data)
dst_file.close()

