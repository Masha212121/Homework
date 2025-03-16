day1 = int(input())
day2 = int(input())
day3 = int(input())
counts = [day1, day2, day3]
repetitions = {}
for value in counts:
    if value in repetitions:
        repetitions[value] += 1
    else:
        repetitions[value] = 1
max_repetitions = max(repetitions.values())
print(max_repetitions)