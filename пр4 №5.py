N = int(input())
K = int(input())

if N < K:
    print(f"{N}")
elif K < N:
    print(f"{K}")
else:
    print(f"Оба рыбака поймали одинаково - по {N}")