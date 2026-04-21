
class emplployee:   #this is the parent class
    company="ITC"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")
    

# class programmer:
#     company="ITC Infotech"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")
    
#     def showlang(self):
#         print(f"the name is {self.name} and the language is {self.language} language")


class programmer(emplployee): #this is the child class and it is inheriting the properties of parent class
    company="ITC Infotech"
    def showlang(self):
        print(f"the name is {self.name} and the language is {self.language} language") 

a=emplployee()
b=programmer()
print(a.company,b.company)