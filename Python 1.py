a= int(input("Enter first number "))
b= int(input("Enter Second number "))

c=int(input("Choose\n1 -> Add\n2 ->Subtract\n3 ->Multiply\n4 ->Divide\n"))
                  
if 1<c<5:
    if c==1:
        print("addition of 2 number is" ,(a+b))
    elif c==2:
        if a>b:
            print("Subtraction of 2 number is" ,(a-b))
        else:
            print("Subtraction of 2 number is", (b-a))
    elif c==3:
        print("Multiplication of 2 number is", (a*b))
    else:
        print("Division of 2 number is" ,'%.3f'%(a/b))

else:
    print("Invalid Selection")
        
    
