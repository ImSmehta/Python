a= int(input("Enter the number "))
if a>1:
    for i in range (2,a):
        if(a%i==0):
            print("Not Prime Number")
            break
    else:
        print("Prime Number")
        
else:
    print("Not prime")
