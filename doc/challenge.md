# 中間課題
pythonによるプログラミング入門の中間課題として，簡易的なプログラムを作成する．

## 成果物: 対話式の二値演算プログラム
仕様については以下の通り．
- CUI
- 対話式
- プログラムからユーザに対して二つの値と演算子を要求する
- プログラムは受け取った情報をもとに演算をして，その結果をユーザに知らせる
- 不正が値が入力された場合は，改めて要求をする
- ユーザが明示的に止めると入力しない限り続行する

![サンプル](img/sample01.png)

## 演習
プログラミングを覚えたての状態では，実装の方法を想像するのは容易ではないため，今回は段階的に課題を用意し，最終的に成果物が完成するような方針とする．

### 小課題-1. ユーザからの入力を受け付ける
- コンソールに，```何か数字を入力してください >> ```と表示してください
- 入力された値を，変数に格納してください
    - ヒント:
        - ```input("好きな文字列")```という関数を用います．
        - ```hoge = input("fugafuga")```と書くと，実行された時に，コンソールに```fugafuga```と表示され，ユーザからの入力を待ち受けます．エンターが押されたとき，ユーザが入力した内容が```hoge```にString型で格納されます．
- その変数中身を，```入力された値は XX です```という形式でコンソールに表示してください
    - ヒント
        - 文字列内に変数を埋め込みたい場合は，```"Hello {} , python".format("world")```という形式で書きます．
            - この場合，```"Hello world , python"```という文字列になます

### 小課題-2. 入力された値が半角数字かどうかを確認する
- ユーザから受け取った値が，半角の数字であるかどうかの判定を行ってください
    - ヒント
        - ```(String型の変数).isascii()```という関数を用います
            - 文字列が半角英数字のみでで構成されていた場合に，```True```を返し，それ以外は```False```を返します．
        - ```(String型の変数).isdecimal()```という関数を用います
            - 文字列が十進数のみで構成されていた場合に，```True```を返し，それ以外は```False```を返します．
- 半角数字だった場合は```入力された値は XX です```という形式でコンソールに表示してください．
- 半角数字以外の値が入力された場合．```不正な入力です```とコンソールに表示してください．

### 小課題-3. 正常な値が入力されるまでやりなおす
- ユーザから受け取った値が，半角の数字でなかった場合，```不正な入力です```とコンソールに表示してください
- 不正な値だった場合，改めてコンソールに，```何か数字を入力してください >> ```と表示してください
    - ヒント
        - 無限ループを使います
        - ```break```という関数を使うことによって，無限ループから抜け出し，ループの外の次の処理に進みます

### 小課題-4. 二つの値を受け取る
- 二つの値をユーザからの入力で順番に受け取って，それぞれ別の変数に格納してください．
    - ヒント
        - 今までの小課題の組み合わせです
- 二つの値を受け取ったら，コンソールに，```入力された値は {} と {} です```と表示してください
    - ヒント
        - ```"Hello {}, {}".format("world", "python")```とした場合，順番に変数が埋め込まれていき，```"Hello world, python"```という文字列になります．

### 小課題-5. 二値の和を計算する
- 受け取った二つの値を足して，コンソールに```AA と BB の和は CC です```という形式で表示してください
    - ヒント
        - 受け取った値は，```String型(文字列型)```なので，見た目が数字だったとしても，単なる文字として扱われます
        - 四則演算ができるのは，原則として```Int型(整数型)```のような数字型のみでです．
        - String型の値をInt型の値に変換するためには，```int("10")```といった書き方をします．この場合，```"10"```は数字型ではなく文字列型ですが，```int("10")```とすることで，```10```という数字型に変換され，四則演算をすることができる値になります．

### 小課題-6. 終了コマンドを受け付ける
- 対話の最後に，```プログラムを続行しますか? (9...はい 0...いいえ) >> ```とコンソールに表示して，ユーザからの入力を受け付けるようにしてください
- 不正な値だった場合は，改めて入力を受け付けてください
    - ヒント
        - 今まで行ってきた小課題の組み合わせで作ることができます．

### +α
- 他の四則演算もできるように拡張してください
- 0除算の場合にどのようにするべきか考えて実装してみてください