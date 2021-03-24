import sys

arg1,arg2,arg3=input("Enter 3 numbers")
if arg1>arg2 and arg1>arg3:
  print("the biggest no is",arg1)
elif arg2>arg1 and arg2>arg3:
  print("the biggest no is",arg2)
else:
  print("the biggest no is",arg3)
