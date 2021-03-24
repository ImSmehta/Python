
sample=['apple','mango','orange','grapes','banana']

print("sample list is: ",sample)


#searching banana keyword in the list using in operator


if 'banana' in sample:
    print("Keyword is present in the list")

else:
    print("Keyword is not present in the list")


#searching banana keyword in the list using for loop


for i in sample:
    if i=='banana':
        print("Keyword is present in the list")
        break
else:
    print("Keyword is not present in the list")
        
        
#printing list in reverse order

print("List in reverse order: ",sample[::-1])        
