import math as mt
n1 = int(input())
n2 = int(input())
minimum = min(n1, n2)
maximum = max(n1, n2)
result = mt.pi*(maximum**2 - minimum**2)
print(result)
