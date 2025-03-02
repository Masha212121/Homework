bitcoin_price = input()
if len(bitcoin_price) >= 3:
    third_digit = bitcoin_price[-3]
    print(third_digit)
else:
    print("Число слишком короткое, третьей цифры справа нет.")