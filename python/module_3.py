"""Module 3: Find the largest prime factor of a given number."""

number = 600851475143
factor = 2

while factor ** 2 <= number:
    while number % factor == 0:
        number = number // factor
    factor += 1

print(number)