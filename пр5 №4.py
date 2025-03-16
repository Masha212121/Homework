def get_parrot_form(number):
    last_digit = number % 10
    if 11 <= number % 100 <= 14:
        return "попугаев"
    if last_digit == 1:
        return "попугай"
    elif 2 <= last_digit <= 4:
        return "попугая"
    else:
        return "попугаев"
try:
    number = int(input())
    if number < 1 or number > 100:
        print("Число должно быть от 1 до 100.")
    else:
        parrot_form = get_parrot_form(number)
        print(f"{number} {parrot_form}")
except ValueError:
    print("Ошибка: введите целое число.")