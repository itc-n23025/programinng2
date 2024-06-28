import argparse
import pprint
import shelve

import pyperclip


def save_clipboard(mcb_shelf, key):
    mcb_shelf[key] = pyperclip.paste()
    print(f"クリップボードの内容をキー '{key}' として保存しました。")


def delete_clipboard(mcb_shelf, key):
    if key in mcb_shelf:
        del mcb_shelf[key]
        print(f"キー '{key}' に対応するクリップボードの内容を削除しました。")
    else:
        print(f"キー '{key}' に対応するクリップボードの内容は存在しません。")


def list_keys(mcb_shelf):
    keys = list(mcb_shelf.keys())
    values = list(mcb_shelf.values())
    values_first_10_chars = [value[:20] for value in values]  #20文字まで表示
    list_keys_dict = dict(zip(keys, values_first_10_chars))
    pprint.pprint(list_keys_dict)


def load_clipboard(mcb_shelf, key):
    if key in mcb_shelf:
        pyperclip.copy(mcb_shelf[key])
        print(f"キー '{key}' に対応するクリップボードの内容を読み込みました。")
    else:
        print(f"キー '{key}' に対応するクリップボードの内容は存在しません。")


def main():
    mcb_shelf = shelve.open('mcb')

    parser = argparse.ArgumentParser(description="テキストの断片をクリップボードに保存したり読み込んだりするプログラム")
    parser.add_argument('action', help="アクションを指定します。'save': 保存, 'delete': 削除, 'list': 一覧表示")
    parser.add_argument('key', nargs='?', help="保存・削除・読み込みするキー（名前）")

    args = parser.parse_args()

    if args.action == 'save':
        save_clipboard(mcb_shelf, args.key)
    elif args.action == 'delete':
        delete_clipboard(mcb_shelf, args.key)
    elif args.action == 'list':
        list_keys(mcb_shelf)
    else:
        load_clipboard(mcb_shelf, args.action)

    mcb_shelf.close()


if __name__ == '__main__':
    main()
