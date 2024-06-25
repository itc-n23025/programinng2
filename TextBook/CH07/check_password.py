import re
def check_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    return True

if __name__ == "__main__":
    passwords = ['abcdehA1', 'abcdeA1', '', '        ',
                 'abcdefgh', 'abcdefgA', 'abcdefg1',
                 'ABCDEFGH', 'ABCDEFGa', 'ABCDEFG1',
                 '12345678', '1234567a', '1234567A']
    for p in passwords:
        print(p + ':' + str(check_password(p)))

