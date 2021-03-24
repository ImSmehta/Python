lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n):
    r = int(input())
    lst.append(r)
      
print(" List is: ",lst)     #original List

print(" Maximum element of list is: " ,max(lst)) # maximum of the list


print(" Minimum element of list is: " ,min(lst)) #min of the list
