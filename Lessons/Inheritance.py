#Inheritance
#A mechanism for resuing code in programming that supports inheritance

class Dog:
    def walk(self):
        print("walk")

class Cat:
    def walk(self):
        print("walk")
#the above is bad and not good for long programs... D.R.Y. DONT REPEAT YOURSELF
# Do not define something twice, do this:

class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    pass #this means omit this line

class Cat(Mammal):
    def meow(self):
        print("meow") #if you dont want to use "pass" then you can still define the method

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.meow() #now when we create the cat1 method and use the "." we have walk() from ineheritance and meow() from defined
