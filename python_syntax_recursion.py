def iteration_factorial(num):
    result = num

    for member in range(1, num):
        result *= member
    return result


def recursion_factorial(num):
    if num == 1:
        return 1
    else:
        return num * recursion_factorial(num - 1)


number = int(input("please input number"))
if number > 10:
    print("number is too bigger")
else:
    print(iteration_factorial(number))
    print(recursion_factorial(number))
