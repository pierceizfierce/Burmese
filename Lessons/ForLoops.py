#For Loops:
#Used to iterate over items a collection such as a string

for item in "Python":
    print(item)
for item in ["mosh", "john", "sarah"]: #the [] is representing a list.
    print(item)
for item in [1,2,3,4,5,6,7]:
    print(item)
for item in range (10): #the built-in funtion "range" in this example will say 0-9.
    print(item)
for item in range (5, 10): #the built-in funtion "range" with a comma in this example will say 5-9.
    print(item)
for item in range (5, 10, 2): #the built-in funtion "range" with a 2 means "step by" in this example will say 5, 7, 9.
    print(item)
prices = [10,20,30]
total = 0
for item in prices:
    total += item
 print(total)
