#
# #While Loops:
# #Used to iterate over code multiple times
#
# # i = 1
# #
# # # while i <= 5: # As long as this condition is true, the code below it will run.
# # #         print(i)
# # #         i = i + 1 # you will need to do something like this to keep from creating an infinite loop
# # # print ("Done")
# #
# # while i <= 5:
# #         print('*' * i)  # When you multiply a string by a number that string will be repeated
# #         i = i + 1
# # print("Done")
# #
# #
# # secret_number = 9
# # guess_count = 0
# # guess_limit = 3
# # while guess_count < guess_limit:
# #         guess = int(input("Guess the number I'm thinking: "))
# #         guess_count += 1
# #         if guess == secret_number:
# #                 print("That is correct! Thanks for playing!")
# #                 break # The "break" statement terminates the loop
# # else:
# #      print("Sorry, you did not guess the number I was thinking. Play again!")
#
# command = "" #this is an "empty string and is used to falsify the variable
# started = False
# #while command != "quit": #the != means does not equal
# while True:
#     command = input("> ").lower() #you can use the dot method here, so you dont have to repeat it throughout the code
#     if command == "start":
#         if started:
#             print("car already started")
#         else:
#             started = True
#             print("The car has started.")
#     elif command == "stop":
#         if not started:
#             print("Car already stopped")
#         else:
#             started = False
#             print("The car has stopped.")
#     elif command == "help":
#         print("""
# start - will start the car
# stop - will stop the car
# quit - quits the program
#         """) #this will create a string block to write what you need
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, please retype your input")
