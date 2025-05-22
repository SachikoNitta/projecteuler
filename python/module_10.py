def main():
    # 2から20000までの数が素数かどうかを示す配列を作成
    #（ややこしいのでインデックス=数とする. 0と1も配列に含まれるが問題ない）
    max_n = 2000000
    is_prime = [True] * (max_n + 1)

    # 
    num = 2
    while num * num < max_n:
        if is_prime[num]:
            # numの倍数は素数ではないので、is_primeをFalseにする
            for i in range(num * num, max_n, num):
                is_prime[i] = False
        num += 1

    # リストのうち値がTRUEのものだけを抜き出す.
    primes = [
        i for i in range(2, max_n) if is_prime[i]
    ]

    # 合計を取得.
    print(sum(primes))

if __name__ == "__main__":
    import time
    start = time.time()
    main()
    end = time.time()
    print("Execution time: ", end - start)