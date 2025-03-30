X = int(input("Введите целое число X: "))
sum = 0
for i in range(1, X+1):
    sum += i
print(f"Сумма первых {X} натуральных чисел равна: {sum}")