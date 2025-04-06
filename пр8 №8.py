def first_sequence():
    print("\nПервая последовательность:")
    num = ""
    for i in range(1, 10):
        num += str(i)
        result = int(num) * 8 + i
        print(f"{num} * 8 + {i} = {result}")

def second_sequence():
    print("\nВторая последовательность:")
    num = ""
    for i in range(1, 10):
        num += str(i)
        result = int(num) * 9 + (i + 1)
        print(f"{num} * 9 + {i + 1} = {result}")

def third_sequence():
    print("\nТретья последовательность:")
    num = ""
    for i in range(1, 10):
        num += "1"
        result = int(num) * int(num)
        print(f"{num} * {num} = {result}")

first_sequence()
second_sequence()
third_sequence()