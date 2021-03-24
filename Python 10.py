a= int(input("Inter first number"))
b= int(input("Inter second number number"))

c=a+b

print("Original Value of c: ", c)
d=int(input("Choose\n 1->ADD\n 2->SUB\n 3->Multiply\n 4->Divide\n 5->MOD\n 6->Expo\n 7->FloorDivision"))

if 0<d<8:
    if d==1:
        c +=a
        print("Addition using assignment operator: ", c)
    elif d==2:
        c -=a
        print("Subtraction using assignment operator: ", c)
    elif d==3:
        c *=a
        print("Multiplication using assignment operator: ", c)
    elif d==4:
        c /=a
        print("Division using assignment operator: ", c)
    elif d==5:
        c %=a
        print("Modulus using assignment operator: ", c)
    elif d==6:
        c **=a
        print("Exponential using assignment operator: ", c)
    else:
        c //=a
        print("Floor Division using assignment operator: ", c)
else:
    print("Invalid Choice")
