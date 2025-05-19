def __main__():
    for a in range(1, 333):
        for b in range(a + 2, (998 - a) // 2):
            # a + b + c = 1000
            c = 1000 - a - b
            if a * a + b * b == c * c:
                print(a, b, c)
                print(a * b * c)
                break
    
if __name__ == "__main__":
    import time
    start = time.time()
    __main__()
    end = time.time()
    print("Execution time: ", end - start)