import math

a = float(input())
b = float(input())
c = float(input())
if a + b > c and a + c > b and b + c > a:
    alfa = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    betta = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
    gamma = math.acos((a**  2 + b **2 - c ** 2) / (2 * a * b))
    alfa_deg = math.degrees(alfa)
    betta_deg = math.degrees(betta)
    gamma_deg = math.degrees(gamma)
print(alfa_deg, betta_deg, gamma_deg)