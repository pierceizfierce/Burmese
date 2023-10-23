#Classes
#Classes are used to define new "types"
#objects are instances of a class. a class is a blueprint and an object is created from that blueprint.
#like building a house (Blueprint and floorplan from blueprint

#simple types:
    #numbers
    #booleans
    #strings
#complex types
    #lists
    #dictionaries

#class ex
    #shopping cart

class Point:   #pascal naming convention. ths is uppercase the first letter of every word. ex. EmailClient
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point1 = Point()
point2 = Point() #each object is a instance of a point class
point1.draw()

point1.x = 10 #objects can also have attributes
point1.y = 20 #these are attributes.. attributes are variables that belong to a particular object

point2.x = 1
point2.y = 2
print(point2.x)

#test
