import math
def can_fit_carpet(A, B):
    diameter = 13.0
    diagonal = math.sqrt(A**2 + B**2)
    return diagonal <= diameter
A = float(input())
B = float(input())
if can_fit_carpet(A, B):
    print("да")
else:
    print("нет")