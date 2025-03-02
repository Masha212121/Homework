import math
N=float(input())
hours=math.floor(N/30)
minutes=math.floor((N%30)/0.5)
print(str(hours) +" "+ str(minutes))