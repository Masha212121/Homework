answer = int(input())
if answer <= 0:
    print("неверно")
else:
    while answer > 1:
        if answer % 2 != 0:
            print("неверно")
            break
        answer = answer // 2
    else:
        print("верно")