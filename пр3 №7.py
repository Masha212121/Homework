raw = input('Enter number: ')
try:
    num = int(raw)
    print(num)
except ValueError:
    print("Введённая строка не является числом. Пожалуйста, введите число.")