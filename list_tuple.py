##### List

### Concatenation (+)
# a = [1, 2]
# b = [3, 4]
# print(a + b)

### Repetition (*)
# print([1, 2] * 3)

### Indexing
# data = [10, 20, 30, 40]
# print(data[0])
# print(data[-1])

### Slicing
# data = [10, 20, 30, 40, 50]
# print(data[1:4])
# print(data[::-1])

### Membership Operators
# data = [10, 20, 30]
# print(20 in data)
# print(100 not in data)

### Functions
# len([1,2,3])
# max([10,20,5])
# min([10,20,5])
# sum([1,2,3])
# sorted([3,1,2])
# list("abc")

### Methods
# lst=[1,2,3,4,5,6]
# lst.append(10)
# lst.extend([1,2])
# lst.insert(1,100)
# lst.remove(10)
# lst.pop()
# lst.clear()
# del lst[0]
# lst.index(20)
# lst.count(10)
# lst.sort()
# lst.reverse()
# sorted(lst)
# lst.copy()

### Nested List
# data = [[1, 2], [3, 4]]
# print(data[0])
# print(data[1][1])

###### TUPLES

## Empty Tuple
# t=()

## Single Element Tuple
# t = (10,)

## Concatenation (+)
# a = (1, 2)
# b = (3, 4)
# print(a + b)

## Repetition (*)
# print((1, 2) * 3)

## Indexing
# data = (10, 20, 30, 40)
# print(data[0]) 
# print(data[-1])

## Slicing
# data = (10, 20, 30, 40, 50)
# print(data[1:4]) 
# print(data[::-1])

## Membership Operators
# data = (10, 20, 30)
# print(20 in data) 
# print(100 not in data)

## Functions
# len((1,2,3))
# max((10,20,5))
# min((10,20,5))
# sum((1,2,3))
# sorted((3,1,2))
# tuple("abc")
# any((0,0,1))
# all((1,2,3))

## Methods
# (1,2,2,3).count(2)
# (10,20,30).index(20)

## TUPLE PACKING
# data = 10, 20, 30
# print(data)

## TUPLE UNPACKING
# data = (10, 20, 30)
# a, b, c = data
# print(a) 
# print(b) 
# print(c)

## NESTED TUPLES
# data = ((1, 2), (3, 4))
# print(data[0]) 
# print(data[1][1])

## IMMUTABILITY OF TUPLES
# data = (10, 20, 30)
# data[0] = 100
# TypeError

## MUTABLE OBJECTS INSIDE TUPLES
# data = (10, [20, 30], 40)
# data[1].append(50)
# print(data)

