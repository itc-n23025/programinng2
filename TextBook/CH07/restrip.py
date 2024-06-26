import re
def restrip(s, chars=r'\s'):
    return re.sub('^[' + chars + ']*(.*?)[' + chars + ']*$', r'\1', s)


if __name__ == '__main__':
    args = [' spam ', ' spam', ' spam ', ' spam ', ' spam ', 'spam spam ']
    for a in args:
        rs = restrip(a)
        ss = a.strip()
        eq = '==' if rs == ss else '!='
        print("restrip('{}')->'{}' {} '{}'.strip()->'{}'".format(a, rs, eq, a, ss))
    args = ['EspamG', 'EspamG', 'EspamEG', ' EspamG ', 'Espam', 'spamE',
            'spam', 'EspamEspamE']
    for a in args:
        rs = restrip(a, 'EG')
        ss = a.strip('EG')
        eq = '==' if rs == ss else '!='
        print(f"restrip('{a}, 'EG')->'{rs}' {eq} '{a}'.strip('EG')->'{ss}'")
