

# for add
class Number:
    def __init__(self, n):
        self.n = n
    def __add__(self, other):
        return self.n + other.n
    
num1 = Number(5)
num2 = Number(10)
print(num1 + num2)  # This will call the __add__ method and return 15


# for subtract
class Number:
    def __init__(self, n):
        self.n = n
    def __sub__(self, other):
        return self.n - other.n
    
num1 = Number(15)
num2 = Number(5)
print(num1 - num2)  # This will call the __sub__ method and return 10

# for multiplication
class Number:
    def __init__(self, n):
        self.n = n
    def __mul__(self, other):
        return self.n * other.n

num1 = Number(5)
num2 = Number(10)
print(num1 * num2)  # This will call the __mul__ method and return 50

# for division
class Number:
    def __init__(self, n):
        self.n = n
    def __truediv__(self, other):
        return self.n / other.n
num1 = Number(10)
num2 = Number(5)
print(num1 / num2)  # This will call the __truediv__ method and return 2.0

# for modulus
class Number:
    def __init__(self, n):
        self.n = n
    def __mod__(self, other):
        return self.n % other.n
num1 = Number(10)
num2 = Number(3)
print(num1 % num2)  # This will call the __mod__ method and return 1

# for exponentiation
class Number:
    def __init__(self, n):
        self.n = n
    def __pow__(self, other):
        return self.n ** other.n
    
num1 = Number(2)
num2 = Number(3)
print(num1 ** num2)  # This will call the __pow__ method and return 8
