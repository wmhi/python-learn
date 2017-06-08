# except syntax
# try:
#   coding
# except Exception[as reason]:
#    error handle coding

# with ... as ... syntax can auto close file,when the file is not be use  
try:
    with open("not_exist_file.txt", "r") as fp:
        for each_line in fp:
            print(each_line)
# The OSerror value is assigned to reason
except OSError as reason:
    print("open file err:" + str(reason))
except TypeError as reason:
    print("open file err:" + str(reason))
except (TabError, TimeoutError) as reason:
    print("open file err:" + str(reason))
finally:
    print("err:")

# "except is like a special "if", it can be used with the "else"
try:
    int("123")
# The OSerror value is assigned to reason
except ValueError as reason:
    print("err:" + str(reason))
else:
    print("success")

# i can use "raise" create a error
# IE:raise ZeroDivisionError
