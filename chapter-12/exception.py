
try:
    a=int(input("Enter a number: "))
    print(f"The number you entered is: {a}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except Exception as e:
    print(e) 