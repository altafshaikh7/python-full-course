a = int(input("Enter your age : " ))
#if elif esle statment
if (a>=18):
    print("You are eligible to vote")

elif(a<0):
    print("Invalid age")    

elif(a==0):
    print("You are enteriing 0, which is not a valid age")

else:
    print("You are not eligible to vote")


print("end of the program")