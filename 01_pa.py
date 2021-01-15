# 1: Write a Python program to read a file line by line and store it into a list.

with open('text.txt','r') as f:
               
    mylist = f.readlines()
    print(mylist)


