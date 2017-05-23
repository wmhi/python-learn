# lamda test, here pycharm tell me "do not assign a lambda expression, use a def", why?
# stack overflow answers:
# The legitimate use case for lambda is where you want to use a function without assigning it, e.g:
# sorted(players, key=lambda player: player.rank)

# tmp = lambda x: x + 1

tmp = list(filter(lambda x: x % 2, range(10)))
print(tmp)

tmp = list(map(lambda x: x * 2, range(10)))
print(tmp)
