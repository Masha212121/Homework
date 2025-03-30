count = 0
prev_temp = None
while True:
    temp = float(input())
    if temp == 0:
        break
    if prev_temp is not None and temp < prev_temp:
        count += 1
    prev_temp = temp
print(count)