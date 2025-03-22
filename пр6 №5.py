def is_knight_move_valid(start, end):
    start_col = ord(start[0]) - ord('a') + 1
    start_row = int(start[1])
    end_col = ord(end[0]) - ord('a') + 1
    end_row = int(end[1])
    col_diff = abs(start_col - end_col)
    row_diff = abs(start_row - end_row)
    return (col_diff == 2 and row_diff == 1) or (col_diff == 1 and row_diff == 2)

start = input().strip().lower()
end = input().strip().lower()

if len(start) != 2 or len(end) != 2 or not start[0].isalpha() or not end[0].isalpha() or not start[1].isdigit() or not end[1].isdigit():
    print("Некорректный ввод. Используйте формат, например, a1 или h8.")
else:
    if is_knight_move_valid(start, end):
        print("верно")
    else:
        print("ошибка")