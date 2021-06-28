
if __name__ == "__main__":
    num = ""

    while True:
        num = input("数字を入力してください >> ")

        if num.isascii() and num.isdecimal():
            print("入力された数字は {} です".format(num))
            break
        else:
            print("入力された値が不正です")