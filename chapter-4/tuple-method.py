
from itertools import count


a=("apple","banana","grape","orange",20,3.5,True,"Altaf","Shaikh")
n=a.count("apple") # count the number of times "apple" appears in the tuple
print(n)

l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
concatenated_list = l1 + l2 # concatenate two lists
print(concatenated_list)

b=(1,2,3,4,5)
# count.append(6) # this will give an error because we can not change the value of tuple
count = b.count(4) # count the number of times 4 appears in the tuple
print(count)


index = b.index(3) # find the index of the first occurrence of 3 in the tuple
print(index)