sec=int(input("Enter time:"))
h=str(sec//3600)
m=(sec//60)%60
s=sec%60
if m<10:
    m="0"+str(m)
else:
    m=str(m)
if s<10:
    s="0"+str(s)
else:
    s=str(s)
print(h+":"+m+":"+s)
