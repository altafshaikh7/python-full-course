# write a python program to diplay user enter a name follow by good afternoon using input() function
# name = input("enter your name: ")
# print("good afternoon " + name)

# write a program to fill in a letter template which looks like below:


letter='''dear <|NAME|> , 
            you are selected !
                <|date|>'''
letter= letter.replace("<|NAME|>", "Altaf shaikh").replace("<|date|>", "20/06/2024")
print(letter)

# write a program to detect double spaces in a string
string = "this is a string with double  spaces"
print(string.find("  "))

# write a program to format the following letter using escape sequence characters
letter = "Dear Altaf,\n\tThis python course is nice.\nThanks!"
print(letter)