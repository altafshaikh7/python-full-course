
#write a program to find the greatest using if else ladder from user input

# a1=int(input("Enter first number: " ))
# a2=int(input("Enter second number: " ))
# a3=int(input ("enter third number: " ))

# if (a1>a2 and a1>a3):
#     print("greatest number of a1" , a1)

# elif(a2>a1 and a2>a3):
#     print("greatest number of a2", a2)

# elif(a3>a1 and a3>a2):
#     print("greatest number of a3", a3 )



# ps 2

a = int (input("enter physics number: "))
b= int(input ("enter maths number:  " ))
c=int(input("enter chemistry number: " ))

total_percentage =(100* (a + b+ c))/300

if (total_percentage>=40 and a>=33 and b>=33 and c>=33 ):
    print("you are passed:", total_percentage) 


else:
    print("you fail, try again next year", total_percentage)
