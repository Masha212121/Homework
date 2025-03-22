def can_isolate_blocks(N, M, K):
    for i in range(1, N):
        if i * M == K or (N - i) * M == K:
            return True
    for j in range(1, M):
        if N * j == K or N * (M - j) == K:
            return True
    return False
N = int(input())
M = int(input())
K = int(input())
if can_isolate_blocks(N, M, K):
    print("успешно")
else:
    print("неосуществимо")