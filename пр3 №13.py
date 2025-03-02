N=int(input())
C=int(input())
X=int(input())
page=((X-1)//(N*C))+1
colon=((X-1)%(N*C)//N+1)
row=(X-1)%N+1
print(page, colon, row)