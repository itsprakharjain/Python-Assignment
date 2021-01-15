# 5: Write a Python program that takes a text file as input and returns the number of words of a given text file.
# Note: Some words can be separated by a comma with no space.

a=input('''Enter a file Name which is present:
(Note- Enter inp.txt) ''')
with open(a,'r') as f:
    data = f.read()
    print(data)
    new_data= data.replace(" ", ",")
    len(data.split(" "))
    print('number of words present in the file')
print(len(data.split(" ")))
print(new_data)
