# python syntax:list
import os

wm_list = [3, "wm", 1.68, "learn"]
logic_list = [1, [2, 3], 3, 1, 123, 1, 1]
campare_list = [1, 5, 3, 4, 2, 6]
print("wm_list is:%s" % wm_list)

# append test only can add one member into end
wm_list.append("25")
print("wm_list is:%s" % wm_list)

# exten test only can add a list into end
wm_list.extend(["love", "$"])
print("wm_list is:%s" % wm_list)

# move member position
temp = wm_list[1]
wm_list[1] = wm_list[4]
wm_list[4] = temp
print("wm_list is:%s" % wm_list)

# remove member
wm_list.remove("learn")
print("wm_list is:%s" % wm_list)

# slice member
print("wm_list is:%s" % (wm_list[3:6]))

# pop member
wm_list.pop()
print("wm_list is:%s" % wm_list)

# clear member
wm_list.clear()
print("wm_list is:%s" % wm_list)

# delete list
del wm_list

# "in" and 'not in" test
print(2 in logic_list)
print(2 not in logic_list)
print(2 in logic_list[1])

# index count test
print(logic_list.count(1))
print(logic_list.index(1))
print(logic_list.index(1, 3, 6))
# reverse sort test
logic_list.reverse()
print(logic_list)

campare_list.sort()
print(campare_list)

campare_list.sort(reverse=True)
print(campare_list)

campare_list.sort(reverse=False)
print(campare_list)

os.system("pause")
