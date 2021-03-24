a=int(input("Enter First the number "))
b=int(input("Enter Second the number "))
c=int(input("Enter Third the number "))
d=int(input("Enter Fourth the number "))

Maxi=0

if a>b and a>c and a>d:
    print("Greatest number is :" ,a)
    maxi=a
elif b>a and b>c and b>d:
    print("Greatest number is :" ,b)
    maxi=b
elif c>a and b<c and c>d:
    print("Greatest number is :" ,c)
    maxi=c
else:
    print("Greatest number is :" ,d)
    maxi=d
    
    
e=int(input("Enter Fifth the number "))

if e>maxi:
    print("Greatest number is :" ,e)   #taking fifth input and comparing with max
else:
    print("Greatest number is :" ,maxi)
