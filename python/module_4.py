
def __main__():
    # ３桁 * 3桁の数：最小の数は10001、最大の数は999 * 999 = 998001
    # ３桁の数：最小は100、最大は989

    # 6桁のパリンドローム数を上から確認
    for i in range (989, 99, -1):
        parindromic_even = make_palindrome(i, True)
        if is_divisible_by_3_digits(parindromic_even):
            print(f"Even: {parindromic_even}")
            return

    # 5桁のパリンドローム数を上から確認
    for i in range (989, 99, -1):
        parindromic_odd = make_palindrome(i)
        if is_divisible_by_3_digits(parindromic_odd):
            print(f"Odd: {parindromic_odd}")
            return

# パリンドローム数を作る.
# ３桁の数の数字を100a + 10b + cとする
# abcba: 10000a + 1000b + 100c + 10b + a
# abccba: 100000a + 10000b + 1000c + 100c + 10b + a
def make_palindrome(x: int, even: bool = False) -> int:
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    if even:
        return 100000 * a + 10000 * b + 1000 * c + 100 * c + 10 * b + a
    else:
        return 10000 * a + 1000 * b + 100 * c + 10 * b + a

# 3桁*3桁になるか大きい方から確認.
def is_divisible_by_3_digits(x: int) -> bool:
    max = 999
    for i in range(max, 100, -1):
        # 元の数の平方根を超えたら終了
        if i * i < x:
            break
    
        # 3桁の数で割り切れるか確認
        if x % i == 0:
            if x // i < 1000:
                return i

    return False

if __name__ == "__main__":
    __main__()