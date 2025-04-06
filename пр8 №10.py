def is_perfect(num):
    if num <= 1:
        return False
    sum_divisors = 1  # 1 - делитель любого числа

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i
            if i != num // i:
                sum_divisors += num // i
    return sum_divisors == num


N = int(input())

for num in range(2, N + 1):
    if is_perfect(num):
        print(num)