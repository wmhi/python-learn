# except syntax
# try:
#   coding
# except Exception[as reason]:
#    error handle coding
try:
    fp = open("not_exist_file.txt", "r")
    fp.close()
# The OSerror value is assigned to reason
except OSError as reason:
    print("open file err:" + str(reason))
except TypeError as reason:
    print("open file err:" + str(reason))
except (TabError, TimeoutError) as reason:
    print("open file err:" + str(reason))
finally:
    print("open file err:")

# i can use "raise" create a error
# IE:raise ZeroDivisionError
