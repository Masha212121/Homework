def can_pass_brick(A, B, C, D, E):
    if (C <= A and D <= B) or (C <= B and D <= A):
        return True
    if (C <= A and E <= B) or (C <= B and E <= A):
        return True
    if (D <= A and E <= B) or (D <= B and E <= A):
        return True
    return False
A = float(input())
B = float(input())
C = float(input())
D = float(input())
E = float(input())

if can_pass_brick(A, B, C, D, E):
    print("да")
else:
    print("нет")
