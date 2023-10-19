# #
# #Dictionaries
# #used to store items that are key value pairs
# #
# #
# customer = {
#     "Name" : "John Smith",
#     "Age" : 30,
# #    "Age" : 40, #each value pair must be unique. this will overwrite what's there before
#    "Is_verified" : True
# }
# print(customer)
# # customer["birthday"] = "Jan 1 1985" #you can add a key value by setting it and defining the variable or default
# # print(customer)
# # print[age] #this is how you call a specific key value. it is case-sensitive.
# # print(customer.get("name")) #the get method will return "None" instead of error
# # print(customer.get("name", "Jack")) #the second is considered a "default Value".
#                                         # if the variable doesn't exist it will enter this for the value
#  #None represents the absence of a value

phone_number = input("Phone: ")
digits = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
 }
output = ""
for number in phone_number:
    output += digits.get(number, "!") + " " #The get() method returns the value of the item with the specified key.

print(output)

########################################################################################################################
########################################################################################################################

#Emoji Converter

message = input(">")
words = message.split(" ")
emoji = {
    ":)" : ":("
}
output = ""
for word in words:
   output += emoji.get(word, word) + " "
print(output)