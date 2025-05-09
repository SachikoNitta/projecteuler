def __main__():
    factors = []

    for i in range(2, 20):
        for j in factors:
            if i % j == 0:
                i = i // j

        if i != 1:
            factors.append(i)

    multipled = 1
    for i in factors:
        multipled *= i
    print(multipled)

if __name__ == "__main__":
    __main__()