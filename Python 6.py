str1= str(input("Enter the string "))

string= str(input("Enter the string "))

for i in range(0,len(str1)):
    print(str1[i],end=" ")
print("Original string is :",str1)


str2=str1[1:-1]

print("Sliced string is :",str2)    #printing sliced string

print("Repeted String is: ",str1*100) #printing repeted string

print("Combined string is: " , str1+ " "+string) #printing combined string
