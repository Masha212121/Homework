N = int(input())
count = 0
power_of_two = 1

while power_of_two < N:
    power_of_two *= 2
    count += 1
print(f"{count}")