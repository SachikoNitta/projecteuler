import time

def __main__():
    # 何個目の素数を取得するか.
    prime_length = 10001
    # 素数のリスト.
    primes = [2]
    # 素数かチェックする数字.
    num = 2

    while len(primes) < prime_length:
        # 素数かどうか.
        isPrime = True

        # 素数リストの小さい方から割り切れるかチェック.
        for prime in primes:
            # 割り切れたら素数ではない.
            if num % prime == 0:
                isPrime = False
                break;
            # 素数リストの素数の平方がチェックする数字より大きくなったら素数とみなす.
            if prime * prime > num:
                break;

        # 素数の場合はリストに追加.
        if isPrime:
            primes.append(num)
        
        # 次の数字をチェック.
        num += 1
    
    # 最後の素数を取得.
    print(primes[-1])

if __name__ == "__main__":
    start = time.time()
    __main__()
    end = time.time()
    print("Execution time: ", end - start)