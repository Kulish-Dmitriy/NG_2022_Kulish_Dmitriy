from datetime import datetime
timefromuser=int(input("Enter time:"))
dt=datetime.fromtimestamp(timefromuser)
print(dt)