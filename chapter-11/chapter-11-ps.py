
class twoDVector:
    def __init__(self ,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"the vector is ({self.i}, {self.j})")

class threeDVector(twoDVector):
    def __init__(self ,i,j,k):
        super().__init__(i,j) #this will call the init method of the parent class
        self.k=k
    def show(self):
        print(f"the vector is ({self.i}, {self.j}, {self.k})")

a=twoDVector(1,2)
a.show()
b=threeDVector(1,2,3)
b.show()


class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("bow bow!")

d=Dog()
d.bark()
