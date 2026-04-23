from functools import reduce
#map
l=[1, 2, 3, 4, 5]

square= lambda n: n * n

squared_list = list(map(square, l))
print (squared_list)


#filter

def even (n):
    if n % 2 == 0:
        return True
    else:      
         return False
    
onlyEven = filter(even, l)
print(list(onlyEven))


#reduce
def add (a, b):
    return a + b
multiply = lambda a, b: a * b
print(reduce(add, l))
print(reduce(multiply, l))