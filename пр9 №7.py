from itertools import permutations

digits = set(range(10))
for s, e, n, d, m, o, r, y in permutations(digits, 8):
    if s == 0 or m == 0:
        continue
    send = s * 1000 + e * 100 + n * 10 + d
    more = m * 1000 + o * 100 + r * 10 + e
    money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
    if send + more == money:
        print(f"SEND = {send}")
        print(f"MORE = {more}")
        print(f"MONEY = {money}")
        break