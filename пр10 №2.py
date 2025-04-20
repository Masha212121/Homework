def can_throw_brick(A, B, C, D, E):
    hole_min = min(A, B)
    hole_max = max(A, B)

    if (min(C, D) <= hole_min and max(C, D) <= hole_max) or \
            (min(C, E) <= hole_min and max(C, E) <= hole_max) or \
            (min(D, E) <= hole_min and max(D, E) <= hole_max):
        return True
    else:
        return False
A = float(input("Введите размер отверстия A (дм): "))
B = float(input("Введите размер отверстия B (дм): "))
C = float(input("Введите размер кирпича C (дм): "))
D = float(input("Введите размер кирпича D (дм): "))
E = float(input("Введите размер кирпича E (дм): "))

if can_throw_brick(A, B, C, D, E):
    print("Да, Бармалей может выбросить кирпич!")
else:
    print("Нет, кирпич не пролезет в отверстие.")