import math

print("Enter the coefficients for the equation")
print("ax^2 + bx + c = 0:")
a=float(input("First number:"))
b=float(input("Second number"))
c=float(input("third number"))

discr=b**2-4*a*c  #find the discriminant
print("Discriminant D = %.2f" % discr)
if discr>0:
    x1=(-b+math.sqrt(discr))/(2*a)
    x2=(-b-math.sqrt(discr))/(2*a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr==0:
    x=-b / (2 * a)
    print("x = %.2f" % x)
else:
    print("No roots")
