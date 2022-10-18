from cmath import sqrt
what1=input("Whats do we do (calculator),(square root):")
if what1=="calculator":
    what2=input("Whats do we do (+),(-).(/),(*),(**),:")
    number1=float(input("number1:"))
    number2=float(input("number2:"))
    if what2 == "+":
        c=number1+number2
        print(c)
    if what2=="-":
        c=number1-number2
        print(c)
    if what2=="/":
        c=number1/number2
        print(c)
    if what2=="*":
        c=number1*number2
        print(c)
    if what2=="**":
        c=number1**number2
        print(c)
if what1=="square root":
    import math
    c=float(input("Number:"))
    print(math.sqrt(c))

