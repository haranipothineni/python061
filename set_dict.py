######### Set

## Empty Set
# s = set()

## Set with Duplicate Values
# data = {10, 20, 30, 20, 10}
# print(data) # {10, 20, 30}

## Membership Operators
# data = {10, 20, 30}
# print(20 in data) 
# print(100 not in data)

## Union
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)

## Intersection
# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a & b)

## Difference
# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a - b)

## Symmetric Difference
# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a ^ b)

## Subset
# a = {1, 2}
# b = {1, 2, 3, 4}
# print(a <= b)

## Superset
# a = {1, 2, 3, 4}
# b = {1, 2}
# print(a >= b)

## Functions
# len({1,2,3})
# max({10,20,5})
# min({10,20,5})
# sum({1,2,3})
# sorted({3,1,2})
# set("hello")
# any({0,1})
# all({1,2,3})

## Methods
# s={1,2,3,4,5}
# s.add(10)
# s.update([20,30])
# s.remove(10)
# s.discard(10)
# s.pop()
# s.clear()
# s.copy()

# a={1,2,3}
# b={2,3,4,5,6}
# a.union(b)
# a.intersection(b)
# a.difference(b)
# a.symmetric_difference(b)
# a.issubset(b)
# a.issuperset(b)
# a.isdisjoint(b)

### Frozen Set
# data = frozenset({10, 20, 30})
# print(data)

######## Dictionary

## Empty Dictionary
# data = {}
# data = dict()

## Accessing Values
# student = {
# "name": "Harani",
# "age": 21
# }
# print(student["name"]) 
# print(student["age"])

## Updating Values
# student["age"] = 23

## Adding New Key-Value Pairs
# student = { "name": "Ravi"}
# student["course"] = "Python"
# print(student)

## Removing Items
# student = {
# "name": "Harani",
# "age": 22
# }
# del student["age"]
# print(student)

## Membership Operators
# student = {
# "name": "Harani",
# "age": 22
# }
# print("name" in student) 
# print("course" not in student)

## FUNCTIONS
# d = {1:2,3:4,5:6}
# len(d)
# max(d)
# min(d)
# sorted(d)
# dict()
# any(d)
# all(d)

## Methods
# d = {"name": "Harani","age": 22}
# d.get("name")
# d.keys()
# d.values()
# d.items()
# d.update({"age":25})
# d.setdefault("city","Hyd")
# d.pop("age")
# d.popitem()
# d.copy()
# d.clear()
# dict.fromkeys(["a","b"],0)

## NESTED DICTIONARIES
# students = {
# "s1": {"name": "Ravi", "age": 22 },
# "s2": {"name": "Teja","age": 21}
# }
# print(students["s1"]["name"])

## MUTABLE VALUES INSIDE DICTIONARIES
# student = {
# "marks": [90, 85, 88]
# }
# student["marks"].append(95)
# print(student)
# {'marks': [90, 85, 88, 95]}

## VALID DICTIONARY KEYS
# data = {
# 101: "Harani",
# 3.14: "Pi",
# True: "Yes",
# "name": "Python",
# (1,2): "Tuple Key"
# }
