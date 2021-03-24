lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n):
    r = int(input())
    lst.append(r)
      
print("original List is: ",lst)   #original List

avg= sum(lst)/len(lst)
print("Average of list is :",avg)   #average list


bellowaverage=0
aboveaverage=0
equalaverage=0


for i in lst:
    if i>avg:
        aboveaverage= aboveaverage+1
    elif i<avg:
        bellowaverage=bellowaverage+1
    else:
        equalaverage=equalaverage+1


print("Numbers equal to avergae number",equalaverage)
print("Numbers less than avergae number",bellowaverage)
print("Numbers greater than avergae number",aboveaverage) 
        
        
