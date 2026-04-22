
try:
    a=int(input("Enter a number: "))
    print(f"The number you entered is: {a}")


except Exception as e:
    print(e) 


else:  #else tab successfully run hoga jab try block me koi exception nahi aayega
    print("No exception occurred.")