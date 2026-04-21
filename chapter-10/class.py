
class Employee:
    language= "py" #This is a class attributes
    salary=1200000

harry =Employee()   
harry.name="harry"  #This is a instance  attribute
print(harry.name, harry.language,harry.salary)

altaf = Employee()
altaf.name ="Altaf Shaikh"
print(altaf.salary,altaf.name,altaf.language)

'''here name is instance attribute and salary and language are class attributes as they directly belong to 
the class '''