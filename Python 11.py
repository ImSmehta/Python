a = int(input("Enter first number "))          
b = int(input("Enter second number "))            
c = 0

c = a & b;        
print ("Value of c is after  Binary AND ", c)

c = a | b;        
print ("Value of c is after Binary OR ", c)

c = a ^ b;        
print ("Value of c is after Binary XOR ", c)

c = ~a;          
print ("Value of c is after Binary Complement", c)

c = a << 2;       
print ("Value of c is after Binary left shift ", c)

c = a >> 2;       
print ("Value of c is after Binary right shift ", c)
