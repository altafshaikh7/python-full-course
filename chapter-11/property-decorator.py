
class employee:
    a =1
    @classmethod 
    def show(cls): 
        print(f"the class attribute of a is {cls.a}")
    @property
    def name(self):
        return f"{self._fname} {self._lname}"
        
    @name.setter
    def name(self, value):
        self._fname = value.split()[0]  # Assuming the name is a single word, we take the first part of the split
        self._lname = value.split()[1]  # Assuming the name is a single word, we take the first part of the split


e= employee()
e.a= 10
e.name="john doe"
print(e.name)
e.show()