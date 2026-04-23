#Q1

try:
    with open ("1.txt","r") as f:
        print(f.read())
except Exception as e:
        print(e)
try:
    with open ("2.txt","r") as f:
        print(f.read())
except Exception as e:
        print(e)
try:
    with open ("3.txt","r") as f:
        print(f.read())
except Exception as e:
        print(e)

print("Thank You ")


# Q2


l=[1,2,3,4,5,6,7,8]

for i,item in enumerate (l):
     if i==2 or i==4 or i==6:
          print(item)