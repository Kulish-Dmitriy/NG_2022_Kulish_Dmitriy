user_seconds=int(input("Enter time:"))
day=str(user_seconds//86400)
hour=str(user_seconds//3600)
minute=(user_seconds//60)%60
second=user_seconds%60
if minute<10:
    minute="0"+str(minute)
else:
    minute=str(minute)
if second<10:
    second="0"+str(second)
else:
    second=str(second)
print(day+":"+hour+":"+minute+":"+second)
