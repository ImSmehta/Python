
index=[1,2,3,4,5,6,7,8,9,10]
name=['Rohit','Kholi','Surya','Iyer','Pant','Hardik','Jaddu','Sundar','Bhuvi','Bumrah']


print("Id of emp are: ",index)     #printing the list of ID
print("name of emp are: ", name)   #printing the list of nme

#printing the list of name from the specific position

print("Name from 4th position to 9th position: ",name[3:9])

print("Name from 3rd position: ",name[2:])

#printing the name on the basic of user input index

d= int(input("Enter index between 1 to 10 which you want to print "))

for i in range(len(index)):
    if d==i:
        print( "Index",index[i-1],"Name",name[i-1])


#printing the repeted id and name on the basic of user input number of repetition
        
n=int(input("Give the number times you wana repeat "))

print("repeted Id of emp are: ",index*n)

print("repeted name of emp are: ", name*n)

#printing the concatinated list

print("concatinated 2 list : ",index+name)

#printing the list side by side

for i in range(len(index)):
  print( "Index",index[i],"Name",name[i])
