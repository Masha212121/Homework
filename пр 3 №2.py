n=int(input())
hour=n//3600
minute=(n%3600)//60
sec=(n%3600)%60
print(hour,'часов',minute,'минут',sec,'секунд')
