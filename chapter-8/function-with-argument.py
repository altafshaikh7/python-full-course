
from unicodedata import name


#using function
def greet (name):
    print ("hello", name )

greet("Sahil") # function call, it will execute the code inside the function and give us the output
    



#using built in function
def greet (name):
    
    name = input("Enter your name: ")
    print ("hello", name )
greet(name) # function call, it will execute the code inside the function and give us the