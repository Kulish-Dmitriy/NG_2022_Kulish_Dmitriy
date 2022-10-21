action_choice=input("Whats do we do (calculator),(square root):")
if action_choice=="calculator":
    action_choice2=input("Whats do we do (+),(-).(/),(*),(**):")
    first_number=float(input("First number:"))
    second_number=float(input("Second number:"))
    if  action_choice2 == "+":
        c=first_number+second_number
        print(c)
    if  action_choice2=="-":
        c=first_number-second_number
        print(c)
    if  action_choice2=="/":
        c=first_number/second_number
        print(c)
    if  action_choice2=="*":
        c=first_number*second_number
        print(c)
    if  action_choice2=="**":
        c=first_number**second_number
        print(c)
if action_choice=="square root":
    user_number=int(input("Enter number:"))
    squre_root=user_number**0.5
    print("Squre root:"+ str(squre_root))
