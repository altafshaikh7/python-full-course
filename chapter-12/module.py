def myfunc():
    print("Hello from myfunc in module.py!")

    myfunc()
    print(__name__) #__name__ is a special variable in Python that holds the name of the current module. When a Python file is run directly, __name__ is set to "__main__". However, when the file is imported as a module in another file, __name__ is set to the name of the module. This allows you to write code that behaves differently when the file is run directly versus when it is imported as a module.
if __name__ == "__main__":
    print("This code is running in the main module.")
   