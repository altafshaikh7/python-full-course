
a= int(input("enter a first number: "))
b= int(input("enter a second number: "))

if b==0:
    raise ZeroDivisionError("Cannot divide by zero") 
else:
    print(f"the division of {a} and {b} is: {a/b}")