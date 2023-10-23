# Modules
# Moduels are files with python code in them
# used to orgnize code into multiple files (reference converters.py)
# Modules should contain all the related functions and classes
from Lessons.utils import find_max
from Lessons import converters, utils
from Lessons.converters import kg_to_lbs
# #ctrl+space after the "import" will show all the functions in the module
# #Above is the way to import specific parts of a module instead of the whole thing:
print(kg_to_lbs(101)) #this is for the specific function from the module called. you don't have to prefix the module
print(converters.lbs_to_kg(70)) #this is from the whole module being imported. Here the module need to be prefixed

utils.find_max() #goes with "import utils"

numbers = [10,3,6,4]
max = find_max(numbers) #the "Shadows built-in name ... " means you're using something already built in python.
                          # this will overwrite the built-in function
maximum = find_max(numbers)
print(max(numbers)) # purple means it's a built-in function




