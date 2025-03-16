def exchange_knuts(N):
    galleons = N // 493
    N = N % 493
    sickles = N // 29
    N = N % 29
    knuts = N
    if galleons > 0:
        print(f"{galleons} галлеонов")
    if sickles > 0:
        print(f"{sickles} сиклей")
    if knuts > 0:
        print(f"{knuts} кнатов")
    if galleons == 0 and sickles == 0 and knuts == 0:
        print("0 кнатов")
N = int(input())
exchange_knuts(N)
