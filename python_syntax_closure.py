# embed function
def function_first(x):
    print("first function be called")

    # here define second function
    def function_second(y):
        print("second function be called")
        return x * y

    # here call second function
    return function_second(x)


print(function_first(4))


# closure function
def function_first(x):
    test_variable = 10
    print("first function be called， test_variable is ", test_variable)

    # here define second function
    def function_second(y):
        nonlocal test_variable
        test_variable += 1
        print("second function be called, test_variable is ", test_variable)
        return x * y

    return function_second


# tmp_function_second store environment of function_second
tmp_function_second = function_first(4)

print(tmp_function_second)
# tmp_function_second continues to do what function_first is not done
print(tmp_function_second(5))

# git hub are ok
