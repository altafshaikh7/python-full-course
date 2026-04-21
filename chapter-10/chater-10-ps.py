
# class progrmmer:
#     comapny="microsoft"
#     def __init__(self,name,salary,pincode):
#         self.name=name
#         self.salary=salary
#         self.pincode=pincode

# a=progrmmer("harry",1200000,411057)
# print(a.name,a.salary,a.pincode,a.comapny) 

# r=progrmmer("rohan",1000000,32100)
# print(r.name,r.salary,r.pincode,r.comapny)



class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the square is {self.n*self.n}")
    
    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"the squareroot is {self.n**1/2}")
        

a=calculator(4)  
a.square()      
a.cube()      
a.squareroot()     


class demo :
      a=4
o=demo()
print(o.a) #print the class attribute because instance attributeis not present
o.a=0 
print(o.a) #print the instance attribute because instance attribute is present
print(demo.a)