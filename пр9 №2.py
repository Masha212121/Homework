import math

number = float(input())

if number <= 2:
    print("Число должно быть больше 2!")
else:
    while number >= 2:
        print(f"{number:.3f}")
        number = math.sqrt(number)