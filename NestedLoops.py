#Nested Loops: add a loop inside another loop


# (x, y)
# (0,0)
# (0,1)
# (0,2)
# (1,0)
# (1,1)
# (1,2)
#
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})') #use a formated string to make it more readable
#                              #in this it will print (x,y)

numbers = [60,20,60,20,60,20,60,60,60,60,60]

# for item in numbers:
#     print ("x" * item) #this is one way to get the result, but other languages dont have this feature
#                        #In Python you can multiply a number by a string.

for item in numbers:
    output = ""
    for count in range(item):
        output += "x"
    print(output)