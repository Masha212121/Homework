print("Определим породу вашей собаки. Отвечайте 'да' или 'нет'.\n")

answer = input("Собака короткошерстной породы? ").lower().strip()
if answer == 'да':

    answer = input("Рост собаки менее 50 см? ").lower().strip()
    if answer == 'да':
        # Вопрос 3 для маленьких короткошерстных
        answer = input("У собаки короткий хвост? ").lower().strip()
        print("\nРезультат: такса" if answer == 'да' else "\nРезультат: бигль")
    else:
        print("\nРезультат: доберман")
else:

    answer = input("Рост собаки менее 50 см? ").lower().strip()
    if answer == 'да':
        print("\nРезультат: шотландский терьер")
    else:

        answer = input("Рост собаки менее 70 см? ").lower().strip()
        if answer == 'да':

            answer = input("У собаки длинные уши? ").lower().strip()
            print("\nРезультат: бассет-хаунд" if answer == 'да' else "\nРезультат: колли")
        else:
            print("\nРезультат: сенбернар")