import math
def calculate_time(N, K, M):
    sessions = math.ceil((2 * N) / K)
    total_time = sessions * M
    return total_time
input_data = input().strip().split()
N, K, M = map(int, input_data)
if N <= 0 or K <= 0 or M <= 0:
    print("Ошибка: все значения должны быть положительными.")
else:
    time = calculate_time(N, K, M)
    print(f"{time}")