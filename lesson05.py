"""
    総まとめ課題その一
    CUIで二値の和を出力する対話式プログラム
    余力があるのであれば，関数に切り出したり，他の演算子もできるようにしたり拡張可能
    クラス化するほどの内容でもないので，一旦はシンプルなスクリプトでいいのではないかと思っている
"""

if __name__ == "__main__":
    loop = 9
    while loop > 0:
        first_num = ""
        second_num = ""

        while True:
            first_num = input("一つ目の数字を入力してください >> ")
            if first_num.isascii() and first_num.isdecimal():
                break
            else:
                print("不正な入力値です")

        while True:
            second_num = input("二つ目の数字を入力してください >> ")
            if second_num.isascii() and second_num.isdecimal():
                break
            else:
                print("不正な入力値です")

        result = int(first_num) + int(second_num)
        print("{} と {} の和は {} です".format(first_num, second_num, result))

        while True:
            cmd = input("プログラムを続行しますか? (9...はい 0...いいえ) >> ")
            if cmd.isascii() and cmd.isdecimal() and \
                (int(cmd) == 0 or int(cmd) == 9):
                loop = int(cmd)
                break
            else:
                print("入力された値が不正です")

