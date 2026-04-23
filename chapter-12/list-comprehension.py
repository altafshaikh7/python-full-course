
mylist=[1,5,6,7,8,9]
squaredlist=[]

# for item in mylist:
    # squaredlist.append(item*item)

#this can be simplified using list comprehension 
squaredlist=[i*i for i in mylist]
print(squaredlist)

