

#printing number from 1 to 100 and reverse list using for loop

lst=[]
for i in range (1,101):
    print(i)
    lst.append(i)


print("Original List using for loop: ", lst)

print("reversed list using for loop: ", lst[::-1])

    
#printing number from 1 to 100 and reverse list using while loop


lst2=[]

i=1
while i<101:
    print(i)
    lst2.append(i)
    i=i+1

print("Original List using while loop: ", lst2)

print("reversed list using while loop: ", lst2[::-1]) 


#printing each character in new line

string='Hellow world'

for i in range(0,len(string)):
    print(string[i])
