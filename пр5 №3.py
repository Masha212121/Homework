def check_number(number):
    if number < 1000 or number > 9999:
        return "Число должно быть четырехзначным!"

    first_digit = number // 1000
    second_digit = (number // 100) % 10
    third_digit = (number // 10) % 10
    fourth_digit = number % 10

    if first_digit == fourth_digit and second_digit == third_digit:
        return "настоящее"
    else:
        return "кривое"
try:
    number = int(input())
    result = check_number(number)
    print(result)
except ValueError:
    print("Ошибка: введите целое число.")