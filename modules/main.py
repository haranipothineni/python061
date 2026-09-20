import my_module
print(my_module.greet("Alice"))
print(my_module.pi)

from my_module import greet
print(greet("Bob"))

import my_module as m
print(m.greet("Charlie"))

