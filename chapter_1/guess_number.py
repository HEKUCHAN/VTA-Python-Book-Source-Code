# 数あてゲーム
# chapter: 1
# url: None
from fileinput import close
import random

# タイトル
print("秘密の数字をあててみよう！[1 ~ 100]")

# 1から100の中でランダムの数字を出してくれる。
secret_number = random.randrange(1, 101)
print("秘密の数字は:", secret_number, "です")

while True:
    try:
        guess_number = input("あなたの予想する数字を入れてください : ")
    except KeyboardInterrupt:
        print("\n諦めちゃうのぉ？〜、そっかぁ。 またね！")
        break

    #数値かどうかを確認
    if guess_number.isdecimal():
        # 文字列型から数値型に変換
        guess_number = int(guess_number)
    else:
        print("自然数を入力してください!")
        continue

    # もし予想した数字と秘密の数字が一緒の場合はゲームを終わらせる
    if guess_number == secret_number:
        print("正解！おめでとう！")
        break

    # どのくらい正解から離れているか計算
    close_number = secret_number - guess_number

    if close_number >= 1:
        if close_number <= 10:
            print("惜しい、もうちょっと大きい！")
            continue
        elif close_number <= 40:
            print("もう少し大きい！")
            continue
        else:
            print("もっと大きい！")
            continue
    else:
        if close_number >= -10:
            print("惜しい、もうちょっと小さい！")
            continue
        elif close_number >= -40:
            print("もう少し小さい！")
            continue
        else:
            print("もっと小さい！")
            continue
