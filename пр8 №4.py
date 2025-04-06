X = int(input())

for n in range(1, X+1):
    current_sum = 0
    expression = ""
    for i in range(1, n+1):
        current_sum += i
        if i > 1:
            expression += " + "
        expression += str(i)
    print(f"{expression} = {current_sum}")