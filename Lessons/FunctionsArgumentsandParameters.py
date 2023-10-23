# # # Functions
# # #are "containers" that do a specific task
# #
# # print()
# # input()
# #
#
# def greet_user(): #always used underline to separate words, lowercase, and be descriptive
#     print("Hi there!")
#     print("welcome aboard!")
#
#
# print("Start")
# greet_user() #the defined function goes above the call for the function. this is the call, above is the define
# print("finish")


########################################################################################################################
########################################################################################################################

#Parameters

#placeholders for receiving information

def greet_user(first_name, last_name): #the parameter will need to be set here
    print(f"Hi there, {first_name} {last_name}!") #then the parameter will need to be set here (if needed)
    print("welcome aboard!")


print("Start")
greet_user("John", "Smith") #this is a parameter "name" being set to "john"
greet_user("Mary", "McMillan") #this will loop through the code twice, once for each parameter
print("finish")
#*******if a function has a parameter, you are required to give it a value***********
#*******arguments are values that you supply to functions****************************
#parameters are the placeholders we define in our functions for recieving informtion*
#   arguments are the information of those parameters
#Postional Arguments are the values set for each argument (1 , 2)
#       positional argument 1 (John) and positional argument 2 (Smith)