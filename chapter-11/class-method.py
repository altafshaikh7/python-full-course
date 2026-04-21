
class employee:
    a =1
    @classmethod #decorator yeh batata hai ki yeh method class method hai
    def show(cls): #cls is used to refer to the class itself, similar to how self is used to refer to the instance
        print(f"the class attribute of a is {cls.a}")

e= employee()
e.a= 10
e.show()
