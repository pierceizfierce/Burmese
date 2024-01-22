birth_year = input('birth year: ')
# print(type(birth_year))
age = 2023 - int(birth_year)
# print(type(age))
print(age)

weight = input("How much do you weigh? (lbs): ")
weight_in_kg = int(weight) / 2.205

print("You weigh", int(weight_in_kg), "kg")


# ''' - triple quotes are used to do multi-line strings, like email messages

# # if you want to get a specific character of a string use [].
# print(xyz[2]) #this will get the second character starting from 0
# print(xyz[-1]) #this will start counting from the end of the string backwards
# print(xyz[4:10}) #This will skip the first 3 characters and end at the 10th
# print(xyz[7:]) #this will start at the 7th character and continue til the end of the string

