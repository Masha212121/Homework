import math

def can_fit_carpet(a, b):
    diameter = 13
    diagonal = math.sqrt(a2 + b2)

    if diagonal <= diameter and a <= diameter and b <= diameter:
        return True
    else:
        return False

a = float(input("Введите длину ковра (A, м): "))
b = float(input("Введите ширину ковра (B, м): "))

if can_fit_carpet(a, b):
    print(f"Ковер {a}x{b} м можно разместить без обрезки!")
else:
    print(f"Ковер {a}x{b} м НЕ помещается без обрезки или подгибов.")