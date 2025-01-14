import random

def generate_secret_number(length):
    """生成指定位數的隨機不重複數字"""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:length]))

def calculate_result(secret, guess):
    """計算猜測結果，返回A和B的數量"""
    A = sum(1 for s, g in zip(secret, guess) if s == g)
    B = sum(1 for g in guess if g in secret) - A
    return A, B

def main():
    print("歡迎來到1A2B遊戲！")
    while True:
        try:
            length = int(input("請輸入想玩的數字位數 (2-9): "))
            if 2 <= length <= 9:
                break
            else:
                print("請輸入2到9之間的數字！")
        except ValueError:
            print("請輸入有效的數字！")

    secret_number = generate_secret_number(length)
    attempts = 0

    print(f"已生成一個{length}位數的隨機數字，請開始猜測！")

    while True:
        guess = input(f"請輸入您的猜測 ({length}位數): ")
        if len(guess) != length or not guess.isdigit() or len(set(guess)) != length:
            print("輸入不合法，請輸入不重複的數字且長度正確。")
            continue

        attempts += 1
        A, B = calculate_result(secret_number, guess)
        print(f"結果: {A}A{B}B")

        if A == length:
            print(f"恭喜你猜對了！總共嘗試了 {attempts} 次。")
            break

if __name__ == "__main__":
    main()

