#write a program to print multiplication table of given number using for loop 
# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")


# write a program to greet all person in a list 'l' and which srtarts with S

l = ["Sahil", "Rohit", "Suman", "Ankit", "Satyam"]
for name in l:
    if name.startswith("S"):
        print(f"Hello {name}!")
