#
# #Keyword Arguments
# #These don't care about position
# #should always come AFTER positional arguments
# def greet_user(first_name, last_name):
#     print(f"Hi there, {first_name} {last_name}!")
#     print("welcome aboard!")
#
#
# print("Start")
# greet_user(first_name="John", last_name="Smith") #this makes it a "keyword argument. mostly used for readability
# calc_cost("Panera Bread", price=50,shipping=5,discount=0.1) #this is an example of keyword arguments
# print("finish")

########################################################################################################################
########################################################################################################################
#
#The Return Statement
#this is mathnmatic and returns the value to the caller of a function
def square(number):
       return number * number #this function returns the value of square()
# result = square(3) #we called the function square() gave it an argument (3) then stored it in a variable "result"
# print(result)
print(square(3)) #this is how you write shorter code with same result
#if you forget to type "return" and get "none" that means there is an absence of a value

# def square(number):
#    print(number * number)
# print(square(3)) # #if you forget to type "return" and get "none" that means there is an absence of a value
#
# #By default all functions in python return "none" unless changed by adding "return" statement


########################################################################################################################
########################################################################################################################

#Create reusable function
# ref. emoji converter tutorial
#Emoji Converter
#
# message = input(">")
# words = message.split(" ")
# emoji = {
#     ":)" : ":("
# }
# output = ""
# for word in words:
#    output += emoji.get(word, word) + " "
# print(output)

# message = input(">")
#

def emoji_converter(message):
   words = message.split(" ")
   emoji = {
       ":)" : ":("
   }
   output = ""
   for word in words:
      output += emoji.get(word, word) + " "
   return output


message = input(">")
print(emoji_converter(message))

#Above is the Long code while below that is the shortened version using functions