def min_stations(N, K, M):
    if K < M:
        clockwise = M - K - 1
    else:
        clockwise = N - (K - M) - 1
    if K > M:
        counter_clockwise = K - M - 1
    else:
        counter_clockwise = N - (M - K) - 1
    return min(clockwise, counter_clockwise)
N, K, M = map(int, input().split())
if K < 1 or K > N or M < 1 or M > N:
    print("Некорректные данные: станции должны быть в диапазоне от 1 до N.")
else:
    result = min_stations(N, K, M)
    print(f" {result}")
