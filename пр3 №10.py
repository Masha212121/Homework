X=int(input())
Y=int(input())
result = min((X % Y == 0) + (Y % X == 0),1)
print(result)