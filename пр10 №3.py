def can_isolate_k_blocks(N, M, K):
    total = N * M
    if K == 0 or K == total:
        return False
    if K > total:
        return False

    if K % N == 0 and (K // N) <= M:
        return True
    if K % M == 0 and (K // M) <= N:
        return True

    if (K > M and (K - M) % (N - 1) == 0) or \
            (K > N and (K - N) % (M - 1) == 0):
        return True

    for a in range(1, N):
        if (K - a * M) > 0 and (K - a * M) % (N - a) == 0:
            return True
    for a in range(1, M):
        if (K - a * N) > 0 and (K - a * N) % (M - a) == 0:
            return True

    return False
N = int(input("Введите N (число строк кварталов): "))
M = int(input("Введите M (число столбцов кварталов): "))
K = int(input("Введите K (желаемое число отделяемых кварталов): "))

if can_isolate_k_blocks(N, M, K):
    print("Да, можно отделить ровно", K, "кварталов!")
else:
    print("Нет, нельзя отделить ровно", K, "кварталов.")