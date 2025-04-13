N = int(input())
if N == 2:
    print(2)
else:
    for d in range(2, int(N ** 0.5) + 1):
        if N % d == 0:
            print(d)
            exit()
    print(N // 2 if N % 2 == 0 else 1)