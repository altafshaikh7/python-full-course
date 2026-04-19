#write a program using a function to find the greatest number of three numbers

# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# c=int(input("Enter the third number: "))
# def greatest (a,b,c):
#     if (a>b and a>c):
#         return a
#     elif (b>a and b>c):
#         return b
#     elif (c>a and c>b):
#         return c
# print (f"The greatest number among is {greatest(a,b,c)}")

#write a python program using function to convert celsius to fahrenheit

f = int(input("Enter the temperature in Fahrenheit: "))
c = 5*(f -32)/9
def fahrenheit_to_celsius (f):
    return 5*(f-32)/9
print (f"The temperature in Celsius is {fahrenheit_to_celsius(f)}")


#write a python program using function to convert celsius to fahrenheit
c = int(input("Enter the temperature in Celsius: "))
f = (c*9/5)+32
def celsius_to_fahrenheit (c):
    return (c*9/5)+32
print (f"The temperature in Fahrenheit is {celsius_to_fahrenheit(c)}")
