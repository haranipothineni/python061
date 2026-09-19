# # Regular function
# def square(x):
#     return x * x
# print(square(5)) # Output: 25
# # Lambda function doing the same thing
# square_lambda = lambda x: x * x
# print(square_lambda(5)) # Output: 25

# # Normal function
# def add(a, b):
#     return a + b
# print(add(3, 5)) # Output: 8
# # Lambda function doing the same thing
# add_lambda = lambda a, b: a + b
# print(add_lambda(3, 5)) # Output: 8

# max_number = lambda a, b: a if a > b else b
# print(max_number(10, 20)) # Output: 20

# numbers = [1, 2, 3, 4, 5]
# # Square each number using map()
# squared = list(map(lambda x: x * x, numbers))
# print(squared) # Output: [1, 4, 9, 16, 25]

# numbers = [1, 2, 3, 4, 5, 6]
# # Get even numbers using filter()
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens) # Output: [2, 4, 6]

# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# # Sum of all numbers using reduce()
# sum_all = reduce(lambda x, y: x + y, numbers)
# print(sum_all) # Output: 15

# grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
# sorted_grades = dict(sorted(grades.items(), key=lambda item:
# item[1]))
# print(sorted_grades)
# # Output: {'Charlie': 78, 'Alice': 85, 'Bob': 92}

# greet = lambda name="Guest": f"Hello, {name}!"
# print(greet("John")) # Output: Hello, John!
# print(greet()) # Output: Hello, Guest!

# def multiply_by(n):
#     return lambda x: x * n
# double = multiply_by(2)
# triple = multiply_by(3)
# print(double(5)) # Output: 10
# print(triple(5)) # Output: 15

# students = [("Rahul", 80),("Anil", 95),("Kiran", 70),("Suresh", 85)]
# result = sorted(students, key=lambda x: x[1])
# print(result)

# students = [("Rahul", 80),("Anil", 95),("Kiran", 70),("Suresh", 85)]
# result = sorted(students, key=lambda x: x[1], reverse=True)
# print(result)

# students = [("Rahul", 80),("Anil", 95),("Kiran", 70),("Suresh", 85)]
# result = sorted(students, key=lambda x: x[0])
# print(result)

# students = [{"name": "Rahul", "marks": 80},{"name": "Anil", "marks": 95},{"name": "Kiran", "marks": 70},{"name": "Suresh", "marks": 85}]
# result = sorted(students, key=lambda x: x["marks"])
# print(result)

# students = [{"name": "Rahul", "marks": 80},{"name": "Anil", "marks": 95},{"name": "Kiran", "marks": 70},{"name": "Suresh", "marks": 85}]
# result = sorted(students, key=lambda x: x["marks"], reverse=True)
# print(result)

# names = ["Ravi", "Alexander", "John", "Sai"]
# result = sorted(names, key=lambda x: len(x))
# print(result)

# names = ["Ravi", "Alexander", "John", "Sai"]
# result = sorted(names, key=lambda x: len(x), reverse=True)
# print(result)

# a = [10, 20, 30]
# b = [1, 2, 3]
# result = list(map(lambda x, y: x + y, a, b))
# print(result)

