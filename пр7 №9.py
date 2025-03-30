N, K, R = map(float, input().split())
day = 1
current_length = N
while current_length < R:
    current_length *= (1 + K / 100)
    day += 1
print(day)