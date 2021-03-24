lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n):
    r = int(input())
    lst.append(r)
      
print("original List is: ",lst)     #original List

print("sliced list is: ",lst[2:8])  # sliced string


lst2= lst*10
print("Repeted list is: ",lst2)     #repeted list

lst3=[98,78,98,465,46]
print("Concatinated list is: ", lst+lst3) #combined list
