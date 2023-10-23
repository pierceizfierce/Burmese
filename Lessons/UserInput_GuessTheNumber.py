#How to request input from the user
import math  # this imports a module for mathematical calculations. "import"  will show a list of modules available

name = input("what is your name? ") #the "input()" function will ask for something then stor it in memory
print ("Hi " + name) #you can only use this (+) syntax with strings
color = input("what is your favorite color? ")
print(name + "'s favorite color is " + color)
want_to_play = input("Do you want to play guess the number?")
if want_to_play == "yes":
    import random
    import math

    # Taking Inputs
    lower = int(input("Enter Lowest number:- "))

    # Taking Inputs
    upper = int(input("Enter Highest number:- "))

    # generating random number between
    # the lower and upper
    x = random.randint(lower, upper)
    print("\n\tYou've only ",
          round(math.log(upper - lower + 1, 2)),
          " chances to guess the integer!\n")

    # Initializing the number of guesses.
    count = 0

    # for calculation of minimum number of
    # guesses depends upon range
    while count < math.log(upper - lower + 1, 2):
        count += 1

        # taking guessing number as input
        guess = int(input("Guess a number:- "))

        # Condition testing
        if x == guess:
            print("Congratulations you did it in ",
                  count, " try")
            # Once guessed, loop will break
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")

    # If Guessing is more than required guesses,
    # shows this output.
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")
else:
    print ("Fine, I didn't want to play anyways! :P ")