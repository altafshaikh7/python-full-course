
class employee:
    a=1

class programmer(employee):
   b=2
class manager(programmer):
   c=3

o=employee()
print(o.a) #print the attribute
# print(o.b) #this will give an error because the instance variable is not present in the parent class

o=programmer()
print(o.a,o.b) #print the attribute of parent class because it is inherited  

o=manager()
print(o.a,o.b,o.c) #print the attribute of parent class because it is inherited