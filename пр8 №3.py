total_income = 0
people_count = 0

while True:
    income = float(input())
    if income == 0:
        break
    total_income += income
    people_count += 1

if people_count == 0:
    print("Нет данных для расчета")
else:
    average_income = total_income / people_count
    print(f" {average_income:.2f}")