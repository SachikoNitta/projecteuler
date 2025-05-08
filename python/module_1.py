"""Module 1: Calculate the sum of multiples of 3 or 5 below 1000."""

# ver.1
multiples = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)

total = sum(multiples)
print(total)

# =======
# ver.2
# 答え = 3の倍数の和 + 5の倍数の和 - 15の倍数の和
total = 3 * 333 * (1 + 333) / 2 + 5 * 200 * (1 + 200) / 2 - 15 * 66 * (1 + 66) / 2
print(int(total))
