import time

# 1000桁の最初のフィボナッチ数字を計算する

def __main__():
    length = 1000
    a, b = 1, 1
    current_index = 2 
    while len(str(b)) < length:
        a, b = b, a + b
        current_index += 1

    print(f"The first Fibonacci number with at least {length} digits is F({current_index}) = {b}.")

if __name__ == "__main__":
    start = time.time()
    __main__()
    end = time.time()
    print(f"Elapsed time: {end - start:.6f} seconds")