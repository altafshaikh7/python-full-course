
class Employee:
    language= "python" #This is a class attributes
    salary=1200000


    def __init__(self):
        print("i am creating an object")

    def getinfo(self):
        print(f"the language is {self.language}.the salary is {self.salary}")
    
    def greet(self):
        print("good morning")
        

harry =Employee()   
harry.language="JavaScript"  #This is a instance  attribute
print( harry.language,harry.salary)


# harry.getinfo()  
harry.greet()
Employee.getinfo(harry)
