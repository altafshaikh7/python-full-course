# write a program to store seven fruits in list by user input and print the list
fruits = []
for i in range(7):
    fruit = input("enter the name of fruit: ")
    fruits.append(fruit)

print("fruits:", fruits)


# write a to accept marks of 6 students and display them in sorted manner
marks = []
for i in range(6):
    mark = int(input("enter the marks of student: "))
    marks.append(mark)
marks.sort() # sort the marks in ascending order
print("sorted marks:", marks)

