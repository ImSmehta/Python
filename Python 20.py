

#Write a program to generate a Fibonacci series of numbers.

n=int(input("Length of series you want to print fibbonaci series "))
a=0
b=1

if n>0:
    for i in range (0,n):
        print(a)
        c=a+b
        a=b
        b=c
    
else:
    print("Invalid Length")
