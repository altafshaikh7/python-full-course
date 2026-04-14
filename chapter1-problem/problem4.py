import os

# specify the directory path
path = "/LinkedIn-Clone"

# get list of files and folders
contents = os.listdir(path)

# print contents
print("Contents of directory:")
for item in contents:
    print(item)