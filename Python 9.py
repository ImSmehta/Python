print("Format of Complex number a+bi ")

x=complex(5,6)
y=complex(2,3)

print("First complex number is: ",x)
print("Second complex number is: ",y)

c=int(input("Choose\n1 -> Add \n2 -> Sub \n3 -> Multiply \n4 -> Divide"))


if 0<c<5:
    if c==1:
        print("Addition of two complex number is: ", x+y)
    elif c==2:
        print("Sub of two complex number is: ", x-y)
    elif c==3:
        print("Multiplication of two complex number is: ", x*y)
    else:
        print("Division of two complex number is: ",x/y)
else:
    print("Invalid choice")
