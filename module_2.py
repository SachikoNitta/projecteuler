"""Module 2: Calculate the sum of even Fibonacci numbers below 4 million."""

nums = [2]
left = 1
right = 2

while right < 4000000:
    total = left + right

    if total % 2 == 0:
        nums.append(total)

    left = right
    right = total

total_all = sum(nums)
print(total_all)