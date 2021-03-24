# printing all prime number in the given range

print("Enter the lower and upper limit to find all the prime number in the given range ")


x=int(input("Enter the lower limit "))
y=int(input("Enter the upper limit "))


for i in range (x,y+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)


#printing a number is prime or not

d=int(input("Choose\n 1--> you want to continue to check whether a number is prime or not\n 2--> Exit "))

if 0<d<3:
    if d==1:
        a=int(input("enter the number "))
        if a>1:
            for i in range (2,a):
                if a%i==0:
                    print("Number is not prime ")
                    break
            else:
                print("Number is prime ")
        else:
            print("Number is not prime ")
    
        
else:
    print("Invalid Choice ")


