def add_comma(lst):
    if len(lst) <= 0:
        return ''
    if len(lst) == 1:
        return lst[0]
    return ','.join(lst[:-1]) + ', and ' + lst[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
s = add_cxomma(spam)
print(s)