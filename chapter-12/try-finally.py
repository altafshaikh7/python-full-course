def main():
    try:
        a=int(input("Enter a number: "))
        print(f"The number you entered is: {a}")
        return


    except Exception as e:
        print(e) 
        return

    finally:  #finally tab run hoga jab try block me koi exception aayega ya nahi aayega aur yeh function me ke liye bhi chalega agar finally hata diye fuction me return statement hoga to finally block run nahi hoga
        print("This will always be executed.")

main()