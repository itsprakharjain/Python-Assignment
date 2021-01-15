# 3: Write a Python program to convert the Python dictionary object (sort by key) to
# JSON data. Print the object members with indent level 4.

import json
mydict = {'Five': 'panch', 'Seven': True, 'Three': 3, 'Two': 4}
print("Python Dictionary:")
print(mydict)
print("\nJSON data:")
print(json.dumps(mydict, sort_keys=True, indent=4))
