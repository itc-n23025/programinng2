import pyperclip
text = pyperclip.paste()

Lines = text.split('\n')
for i in range(len(Lines)):
    lines[i] = '* ' + lines[1]

text = '\n'.join(lines)

pyperclip.copy(text)