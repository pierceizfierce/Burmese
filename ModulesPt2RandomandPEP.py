#Modules pt.2 - Generating random values

#search python3 module index in google.

#this is a built in module and can be found in: External libraries > python 3.x >
#> pythonsoftwarefoundation.python 3.x (library root) > Lib
#PEP (Python Enhancement Proposal, the warnings that pop up) is a guide for best uses in Python
import random
# # for i in range(3):
# #     print(random.random())
# #     print(random.randint(10,20))
# members = ['john', 'jack','mary','damori']
#
# #remember to store the result in a variable
# leader = random.choice(members)
#
# print(leader)

########################################################################################################################

# dice = (1,2,3,4,5,6)
# roll = random.choice(dice)
# roll2 = random.choice(dice)
# print((roll, roll2))

########################################################################################################################

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


dice = Dice()
print(dice.roll())

