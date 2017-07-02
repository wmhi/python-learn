# Object equals attribute plus method

# Classes must begin with a capital letter

# Encapsulated object
import random


class Turtle:
    # attribute
    color = "green"
    weight = 10
    legs = 4
    shell = True
    mouth = True

    # method ，@staticmethod：http://www.cnblogs.com/caoguo/p/4908711.html
    @staticmethod
    def move():
        print("Turtle is climbing")


# Use the method of the object
turtle = Turtle()
turtle.move()


# Inherit the parent object


class ChildTurtle(Turtle):
    # Pass means that Child_turtle doesn't do anything
    pass


child_turtle = ChildTurtle()
child_turtle.move()


# polymorphic:Different objects have different methods
# ie:Both tigers and turtles can move, but in different ways

# if you have no use "self", you must add  @staticmethod
# because You don't need to instantiate the object, this
# method has nothing to do with the object

#  __init__(self, parameter1, parameter2...)
# The __init__ is automatically called when the object is instantiated


class Tiger:
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def run(self):
        self.x += random.randint(0, 3)
        self.y += random.randint(0, 3)

        print("position:[%d, %d]" % (self.x,  self.y))


class SuperTiger(Tiger):
    def __init__(self):
        # super().__init__() will call derive class __init__
        super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            self.hungry = False
            print("eat")
        else:
            print("I'm not hungry")

    def get_hungry(self):
        return self.hungry

    def set_hungry(self, hungry_state):
        self.hungry = hungry_state

    def del_hungry(self):
        del self.hungry

    # you can use property(fget=None, fset=None, fdel=None, doc=None)
    # This is a little bit like a c function pointer with a structure, than use hungry_state as API
    hungry_state = property(get_hungry, set_hungry, del_hungry, "I\'m the \'hungry\' property.")

super_tiger = SuperTiger()
#
super_tiger.run()
super_tiger.run()
super_tiger.eat()
super_tiger.eat()

print(issubclass(SuperTiger, Tiger))
print(isinstance(super_tiger, (SuperTiger, Tiger)))
print(hasattr(super_tiger, "hungry"))

# if "hungry" doesn't exist, getattr will print "the attribute you get don't exist"
print(getattr(super_tiger, "hungry", "the attribute you get don't exist"))
setattr(super_tiger, "hungry", True)
print(getattr(super_tiger, "hungry", "the attribute you get don't exist"))
# you can use "delattr" delete attribute, ie:delattr(super_tiger, "hungry")

super_tiger.hungry_state = False
print("hungry:" + str(super_tiger.hungry))

# private and public variable
# private variable must be get by method


class Private:
    # use __ as a private flag
    __name = "wm"

    def name(self):
        return self.__name

me = Private()
print(me.name())
