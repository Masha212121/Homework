n = int(input("Введите количество ступеней N: "))

for i in range(1, n + 1):
    # Печатаем пробелы перед звёздочками
    print("  " * (n - i), end="")
    # Печатаем звёздочки для текущей ступени
    print("* " * i)