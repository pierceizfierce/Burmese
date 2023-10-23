import math  # this imports a module for mathematical calculations. "import"  will show a list of modules available
#
birth_year = input('birth year: ')
print(type(birth_year))
age = 2023 - int(birth_year)
print(type(age))
print (age)

weight = input("How much do you weigh? (lbs): ")
weight_in_kg = int(weight) / 2.205

print("You weigh " + weight + "kg")

#''' - triple quotes are used to do multi-line strings, like email messages

# if you want to get a specific character of a string use [].
print(xyz[2]) #this will get the second character starting from 0
print(xyz[-1]) #this will start counting from the end of the string backwards
print(xyz[4:10}) #This will skip the first 3 characters and end at the 10th
print(xyz[7:]) #this will start at the 7th character and continue til the end of the string


# #formatted strings
first = "John"
last = "Smith"
#
msg = f"{first} [{last}] is a coder" #this is an example of a formatted string.
#the "f" tells the syntax this is a formatted string
print(msg)

# Strings Cont.
course = "Python for Beginners"

len(xyz) #calculate length of characters in a string. Useful for input limits, etc.
course.upper() #the dot-method (.) is a method specific to a string.
#Like "?" in Cisco typing a "." after a string (or anything that has methods available to use)
    #will show what methods are available
#In contrast Functions are like print(), len(), etc. they are "general purpose", meaning
    #they don't belong to anything
print (course.find("Z")) #this will return the INDEX of the FIRST occurrence of the reference. Case-sensitive
    #-1 means there is no mention of the reference
print(course.replace("Beginners","New Beginners")) #use Comma "," to say change this to this. Also, Case Sensitive
print("Python" in course) #"in" is a Boolean expression that check for a reference. "Find" returns the index

# Arithmatic Operators
print(10+3) # add
print(10-3) # sub
print(10/3) # div #float
print(10//3) #div integer
print(10%) #modular: the remainder of division
print(10**3) #exponents

x = 3
x = x + 3
x += 3 # augmented assignment operator. same as above but shortened for readability
print(x)

# All languages recognize PEMDAS
x = (2 + 3) * 10 - 3 #() will take priority just like in math
print(x)

x = 2.9
print(round(x))  # round to the nearest integer
print(abs(-2.9)) # this is "absolute" it always returns a positive number


math.ceil(2.9)  # since the "import math" module is enabled at the top of the code sheet, "math." is now enabled for
                    # arithmetic expressions
