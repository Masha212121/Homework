import math
while True:
    num = int(input("Введите число: "))
    root = math.isqrt(num)  # Целочисленный квадратный корень

    if root * root == num:
        print(f"Число {num} является полным квадратом ({root} × {root})")
        break
    else:
        print(f"Число {num} не является полным квадратом")
        print("Попробуйте другое число\n")