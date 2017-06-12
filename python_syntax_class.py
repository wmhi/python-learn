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
# beacuse You don't need to instantiate the object, this
# methon has nothing to do with the object
class Tiger:
    def move(self, name):
        print(name + "i/'m run" + self)
