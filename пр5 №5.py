height = float(input()) / 100
weight = float(input())
bmi = weight / (height ** 2)
if bmi < 16:
    interpretation = "выраженный дефицит массы тела"
elif 16 <= bmi < 18.49:
    interpretation = "недостаточная масса тела"
elif 18.5 <= bmi < 24.99:
    interpretation = "норма"
elif 25 <= bmi < 29.99:
    interpretation = "избыточная масса тела"
elif 30 <= bmi < 34.99:
    interpretation = "ожирение первой степени"
elif 35 <= bmi < 39.99:
    interpretation = "ожирение второй степени"
else:
    interpretation = "ожирение третьей степени"
print(f"{interpretation}")
