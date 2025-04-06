print("Какие два слова передал первой радиограммой Александр Попов?")

first_word = input("Первое слово: ")
second_word = input("Второе слово: ")

correct_first = "Генрих"
correct_second = "Герц"

if first_word == correct_first and second_word == correct_second:
    print("Верно")
else:
    print("Неверно")