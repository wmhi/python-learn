# Object equals attribute plus method

# Classes must begin with a capital letter

# Encapsulated object


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
    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name + ' run')


tiger = Tiger("wm")
tiger.run()


# private and public variable
# private variable must be get by method

class Private:
    __name = "wm"

    def name(self):
        return self.__name

me = Private()
print(me.name())
