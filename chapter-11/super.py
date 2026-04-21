
class employee:
   def __init__(self):
      print("constructor of employee")
   a=1  
    
class programmer(employee):
   def __init__(self):
      print("constructor of programmer")
   b=2
class manager(programmer):
   def __init__(self):
      super().__init__() #this will call the constructor of programmer class and it will print the statement of programmer class        
      print("constructor of manager")
   c=3

# o=employee()
# print(o.a) #print the attribute


# o=programmer()
# print(o.a,o.b) #print the attribute of parent class because it is inherited  

o=manager()
print(o.a,o.b,o.c) #print the attribute of parent class because it is inherited