count = 0
while True:
    N = int(input())
    if N == 0:
        break
    if N >= 4 and N % 2 == 0:
        count += 1
print(count)