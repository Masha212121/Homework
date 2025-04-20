def is_knight_move_valid(x1, y1, x2, y2):
    if not all(1 <= coord <= 8 for coord in [x1, y1, x2, y2]):
        return False
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)
x1 = int(input("Введите начальную позицию коня (x1, 1-8): "))
y1 = int(input("Введите начальную позицию коня (y1, 1-8): "))
x2 = int(input("Введите конечную позицию коня (x2, 1-8): "))
y2 = int(input("Введите конечную позицию коня (y2, 1-8): "))

if is_knight_move_valid(x1, y1, x2, y2):
    print("Ход коня правильный!")
else:
    print("Ход коня невозможен.")