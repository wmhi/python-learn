# dictionary just like remap in linux
# 3 ways to define dictionary

dictionary_1 = {"wm": "me", "hlh": "ok"}
dictionary_2 = dict((("wm", "me"), ("hlh", "ok")))
dictionary_3 = dict(wm="me", hlh='ok')


print(type(dictionary_1), list(dictionary_1), dictionary_1)
print(type(dictionary_2), list(dictionary_2), dictionary_2)
print(type(dictionary_3), list(dictionary_3), dictionary_3)

# use key[hlh] to change value[ok]
dictionary_1["hlh"] = "girl"

# add new key
dictionary_1["Edison"] = "talent"

print(type(dictionary_1), list(dictionary_1), dictionary_1)

# test fromkeys dict.key dict.items
# create dict, fromkeys just like memset, set all member = "h"(The second parameter)
dictionary_4 = {}
dictionary_4 = dictionary_4.fromkeys(range(10), "h")

# traverse keys
for key in dictionary_4.keys():
    print(key)
# traverse items
for item in dictionary_4.items():
    print(item)

# is it in the dictionary
print(dictionary_4.get(11, "NULL"))
print(11 in dictionary_4)
print(11 not in dictionary_4)

# copy, assignment just like pointer, dictionary_4 and dictionary_map point the same address
# but copy is create a new dictionary, id() can get address
dictionary_map = dictionary_4
dictionary_back = dictionary_4.copy()
print(id(dictionary_4))
print(id(dictionary_map))
print(id(dictionary_back))

# pop(key):According to the key pop item, popitem():Random pop a item
dictionary_map.pop(0)
print(dictionary_4)
print(dictionary_map)

dictionary_map.popitem()
print(dictionary_4)
print(dictionary_map)

# setdefault
dictionary_map.setdefault("wm")
dictionary_map.setdefault("love", "hlh")
print(dictionary_map)

# update
dictionary_back.update(dictionary_map)
print(dictionary_back)

# clear dictionary
dictionary_4.clear()
print(dictionary_4)
print(dictionary_map)
