# python: if syntax

input_str = input("please input you grade")
grade = int(input_str)
if 0 <= grade < 60:
    print("level:C")
elif 60 <= grade < 80:
    print("level:B")
else:
    print("level:A")
input("please enter any key to quit")
