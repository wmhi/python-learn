# test global variable and local variable

global_variable = 0

def print_variable():
    local_variable = 1
    # you can't change global variable, beacuse python auto create a local variable in here,
    # which also name "global_variable "
    global_variable = 1
    print("local_variable = ", local_variable, "global_variable = ", global_variable)

print_variable()

def print_global_variable():
    global global_variable
    print("global_variable = ", global_variable)

print_global_variable()
