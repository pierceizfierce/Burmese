# #Lists
# #
# # name = ['jon', 'mark', 'mary', 'sarah']
# #
# # print(name[0])  #this will print the first name in the list
# # print(name[-2]) #this will print the second to the last name in the list.
# #                 #Because of the negative, it will start from the end of the list
# # print(name[2:]) #this will get the range starting from mary (remember 0,1,2 is the sequence)
# # print(name[:3]) #gets the end 3
# # print(name[:]) #default 0:0
# # name [0] = "john"  #this sets the reference to the new reference value
# # print(name)
#
numbers = [100,2,34,40,65,34]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# ########################################################################################################################
# ########################################################################################################################
#
# # Tuples
# # used to store a list of items, but cant be changed. they are immutable
#
# number = [1, 2, 3]  # this is a list
# numbers = (1, 2, 3)  # this is a tuple
# # numbers.  #you will see that the methods have changed and there's no append, remove, etc.
# # the underlined methods (__init__ for example) are called "Magic methods" and are a part of alot of the functions.
# # these are covered in a different lesson
# print(numbers[2])  # you still call them the same way as lists, with square brackets[]
#
# ########################################################################################################################
# ########################################################################################################################
#
# #Unpacking
# #
# coordinates = (1,2,3)
#
# coordinates[0] * coordinates[1] * coordinates[2]
#
# #better way to do this:
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
#
# x * y * z
#
# #best way to do this:
#
# x,y,z = coordinates #shorthand to achive the same results as above.
# #this taks each index and assigns it to the corresponding variable
# #this also works with lists
#
# print(coordinates)