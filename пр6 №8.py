def get_digit_at_position(N):
    sequence = [0]
    for number in range(1, 201):
        for digit_char in str(number):
            sequence.append(int(digit_char))
    if N < 1 or N > len(sequence):
        return "Некорректный номер"
    return sequence[N - 1]
N = int(input())
digit = get_digit_at_position(N)
print(f"{digit}")