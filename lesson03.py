
if __name__ == "__main__":
    num = input("数字を入力してください >> ")
    print("入力された値は {} です".format(num))

    # 半角数字のみで構成された文字列であるかの判定
    # ascii判定に関する参考資料　https://docs.python.org/ja/3/library/stdtypes.html#str.isascii
    # 文字列が数字であるかの参考資料 https://docs.python.org/ja/3/library/stdtypes.html#str.isdecimal
    # isdecimal vs isdigit vs isnumericに関する話は調べれば簡単に出てくるので割愛
    if num.isascii() and num.isdecimal():
        print("入力された値は整数です")
    else:
        print("入力された値は整数ではありません")