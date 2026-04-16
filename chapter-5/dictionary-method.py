marks={
    "harry": 50,
    "shubham":60,
    "rohan":34,
    0:"hello"
} 

print(marks.items())

print(marks.keys())
print(marks.values())

marks.update({"harry": 70})
print(marks)

print(marks.get("harry")) #agar mai isme koi bhi value daalo jo dictionary me available nhi to none print hoga 
# print(marks["harry"])  # aur  isme disctionary me available nhi hoga to error aayega 