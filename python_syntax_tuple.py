# syntax syntax:tuple
# tuple is a special list, it't value of member can't be change or del

tuple_1 = (1, 2, 3)

# you can't use "()" to create a duple, but comma can do this ,like a = (1,) b = 1, a and b both a tuple
tuple_2 = (1)

# create a empty tuple
tuple_3 = ()

# print variable type
print(type(tuple_1))
print(type(tuple_2))
print(type(tuple_3))

# add member to tuple
tuple_1 = tuple_1[:2] + (4,) + tuple_1[2:]
print(tuple_1)
