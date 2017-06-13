# this is the fisrt function from wm
import random


def first_function():
    print("hello world")
    print("this first function from wm")
    print("i'm very excited")


first_function()

# this is the second function from wm
first = random.randint(1, 10)
second = random.randint(1, 10)


def second_function(first, second):
    print(first, second)


second_function(first, second)


# add function document

def function_doc():
    # this comment won't be print, beacuse it not a part in document
    """this is test to print documnent"""
    print("this is print, not document")


function_doc()
# __doc__ doesn't work
function_doc.__doc__

help(function_doc)


# Specify the parameter
def specify_paramter(name, love):
    print(name + "->" + love)


specify_paramter(love="love", name="wm")


# set default parameter
def defualt_parameter(name="wm", love="**"):
    print(name + "->" + love)


defualt_parameter()
defualt_parameter("hlh")
defualt_parameter(love="--", name="hlh")


# test "*" type parameter
def function_with_one_star(*t, except_member):
    print(t, type(t), "except = ", except_member)


def function_with_two_stars(**d):
    print(d, type(d))


function_with_one_star(1, 2, 3, except_member="hello")
function_with_two_stars(a=1, b=2, c=3)


def find_max(*num):
    # 遍历参数列表，判断参数类型是否为整形
    for iterm in num:
        if not isinstance(iterm, int):
            return iterm, '参数错误,参数必须为整数'
    return max(num), min(num)


print(find_max(124232, 1234, 23, 42, 3, 1, 23, 123, 23, 123123, 123123))
