def __main__():
    # a + b + c = 1000 で　a < b < c なので、aは最大で332
    for a in range(1, 332):
        # a < bなのでbは最小でa + 1
        # b < cなので、bは最大で(1000 - a - 1) // 2
        for b in range(a + 1, (1000 - a - 1) // 2):
            if a + b >= 1000:
                break
            
            # a + b + c = 1000
            c = 1000 - a - b

            # a < b < c
            if c <= b:
                break

            # a^2 + b^2 = c^2
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