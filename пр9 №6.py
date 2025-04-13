for AB in range(10, 100):
    CAB = AB * AB
    if CAB >= 100 and CAB % 100 == AB:
        print(CAB)
        break