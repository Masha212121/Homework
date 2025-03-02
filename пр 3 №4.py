s=input()
x,y,n=s.split() #x,y,n стали строками
x=int(x)#перевели в числовой вид
y=int(y)
n=int(n)
price=x*100+y
profit=price*n
r=profit//100
k=profit%100
print(r,'руб.',k,'коп.')
