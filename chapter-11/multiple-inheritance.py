
class emplployee:   #this is the parent class
    company="ITC"
    name="default name "
    def show(self):
        print(f"the name is {self.name} and the company is {self.company}")
    

class coder :
    language="python"
    def printlanguages(self):
        print(f"out of all the languages {self.language} is the best language")


class programmer(emplployee, coder): #this is the child class and it is inheriting the properties of parent class
    company="ITC Infotech"
    def showlang(self):
        print(f"the name is {self.company} and the language is {self.language} language") 

a=emplployee()
b=programmer()
print(a.company,b.company)

b.show() #this will give an error because the instance variable is not present in the child class
b.printlanguages()
b.showlang()