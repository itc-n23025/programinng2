import shelve
import sys

import pyperclip


class ClipboardManager:
    def __init__(self, db_filename):
        self.db_filename = db_filename
        self.mcb_shelf = shelve.open(db_filename)

    def save_to_clipboard(self, key):
        """クリップボードの内容を保存する"""
        self.mcb_shelf[key] = pyperclip.paste()

    def load_from_clipboard(self, key):
        """クリップボードの内容を読み込む"""
        if key in self.mcb_shelf:
            pyperclip.copy(self.mcb_shelf[key])

    def list_keys(self):
        """キーの一覧をクリップボードにコピーする"""
        key_list = list(self.mcb_shelf.keys())
        pyperclip.copy(str(key_list))

    def close(self):
        """データベースを閉じる"""
        self.mcb_shelf.close()


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <command> [arguments]")
        return

    command = sys.argv[1].lower()
    db_filename = 'mcb.db'
    manager = ClipboardManager(db_filename)

    if command == 'save' and len(sys.argv) == 3:
        manager.save_to_clipboard(sys.argv[2])
    elif command == 'list':
        manager.list_keys()
    elif len(sys.argv) == 2:
        manager.load_from_clipboard(sys.argv[1])

    manager.close()


if __name__ == "__main__":
    main()
