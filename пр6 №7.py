def can_order_sushi(K):
    for y in range(K // 7 + 1):
        remaining = K - 7 * y
        if remaining % 5 == 0:
            return True
    return False
K = int(input())
if can_order_sushi(K):
    print("да")
else:
    print("нет")