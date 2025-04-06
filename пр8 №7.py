while True:
    user_input = input("Введите число: ")

    if user_input.isdigit():
        number = int(user_input)
        print(f"Введено целое число: {number}")
        break

    if user_input.startswith('-') and user_input[1:].isdigit():
        number = int(user_input)
        print(f"Введено целое число: {number}")
        break

    print("Ошибка. Попробуйте еще раз.")