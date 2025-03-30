input_str = "alphebetical"
output_str = ""

for i in range(len(input_str)):
    if i % 3 == 2:  # Каждый 3-й символ (индексы 2, 5, 8...)
        output_str += input_str[i]

print(output_str)