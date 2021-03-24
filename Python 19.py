

#Using loop structures print even numbers between 1 to 100.

#By using For loop, use continue/ break/ pass statement to skip odd numbers.

for i in range (1,101):
    if i%2!=0:
        continue
    print(i)

print('\n')

#Break the loop if the value is 50

for i in range (1,101):
    if i==50:
        break
    print(i)

print('\n')

#Use continue for the values 10,20,30,40,50

for i in range (1,101):
    if i==10 or i==20 or i==30 or i==40 or i==50:
        continue
    print(i)

print('\n')

#By using while loop, use continue/ break/ pass statement to skip odd numbers.


i=1
while i<101:
    if i%2!=0:
        i=i+1
        continue
    
    print(i)
    i=i+1
        
print('\n')


#Break the loop if the value is 90


i=1
while i<101:
    if i==90:
        i=i+1
        break
    
    print(i)
    i=i+1

print('\n')


#Use continue for the values 60,70,80,90

i=1
while i<101:
    if i==60 or i==70 or i==80 or i==90:
        i=i+1
        continue
    
    print(i)
    i=i+1

print('\n')






