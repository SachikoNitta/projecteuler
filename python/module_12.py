


def __main__():
    n = 1
    added = 2
    while True:
        # 約数の個数が500以上ならbreak
        if hasFactorsMoreThan500(n):
            break

        # 次の三角数に進む.
        n = n + added
        added += 1
        
    print(n)

def hasFactorsMoreThan500(n):
    count = 0
    f = 1
    while f * f <= n:
        if n % f == 0:
            count += 2
            if count > 500:
                return True
        f += 1
    return count > 500

if __name__ == "__main__":
    import time
    start = time.time()
    __main__()
    end = time.time()
    print("Execution time: ", end - start)
