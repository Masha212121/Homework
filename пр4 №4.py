print("Вы поедете на бал?")
answer = input("Ответ: ")

if not ("да" in answer or "нет" in answer):
    print("Верно")
else:
    print("Неверно")