#Constructors


#Contructor is a function that gets called at the time of creating an object

class Point:
    def __init__(self, x, y): #this method is a contructor, it's used to create an object.
                                    #"self" tells python to reference this object
        self.x = x #this tells python to set the ".x" attribute to reference the "x" argument
       #point.x=10 (this is what it would look like below if you didnt use constructors)
        self.y = y
        #all this above is the same as explicity saying point.x = x.
            #but you initialize the function, then enter the values later like below
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point = Point(10,20)
point.x = 11 #you can also change the value by doing this below the constructor
print(point.x)

########################################################################################################################
class Person:
    def __init__ (self, name):
        self.name = name


talk = Person("John")


print(talk.name)

##Also:

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("talk")


john = Person("John Smith")
john.talk()
print(john.name)

#Extra


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am  {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()