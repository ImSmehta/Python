a= int(input("Enter first number "))
b= int(input("Enter Second number "))
c= int(input("Enter third number "))

if a>b and a>c:
    print("Greated number is",a)
elif b>c and b>a:
    print("Greated number is",b)
else:
    print("Greatest number is",c)
