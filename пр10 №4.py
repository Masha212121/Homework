def get_chess_square_color(column, row):

    if not (1 <= column <= 8 and 1 <= row <= 8):
        return "Ошибка: координаты должны быть от 1 до 8"

    if (column + row) % 2 == 0:
        return "Чёрный"
    else:
        return "Белый"


column = int(input("Введите номер столбца (a-h → 1-8): "))
row = int(input("Введите номер строки (1-8): "))

print(f"Клетка ({column}, {row}) — {get_chess_square_color(column, row)}")