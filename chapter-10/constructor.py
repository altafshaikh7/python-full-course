
class Employee:
    language= "python" #This is a class attributes
    salary=1200000


    def __init__(self, name, salary, language):  #dunder method which is automatically called when we create an object of the class
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")

    def getinfo(self):
        print(f"the language is {self.language}.the salary is {self.salary}")

    @staticmethod
    def greet(self):
        print("good morning")
        

harry =Employee("Altaf",1300000,"JavaScript") 
# harry.name="harry"  #This is a instance  attribute   
print( harry.name ,harry.salary,harry.language)

# rohan = Employee()
