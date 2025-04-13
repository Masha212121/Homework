import math
def count_sum_of_squares(x):
    count = 0
    max_a = int(math.isqrt(x))
    for a in range(1, max_a + 1):
        remainder = x - a * a
        if remainder <= 0:
            continue
        b = math.isqrt(remainder)
        if b * b == remainder and a <= b:
            count += 1
    return count

x = int(input())
print(count_sum_of_squares(x))