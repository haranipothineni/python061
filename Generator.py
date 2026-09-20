# def my_gen():
#     yield 1
#     yield 2
#     yield 3
# gen = my_gen()  # This doesn't run the function, it just prepares the generator
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))  # Output: 3

# # Using for loop on generator
# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
# for i in countdown(3):
#     print(i)

# def greet():
#     yield "Hello"
#     yield "How are you?"
# g = greet()
# print(next(g))  # Hello
# print(next(g))  # How are you?

# # What is next()?
# gen = (x*x for x in range(1, 4))
# print(next(gen))  # 1
# print(next(gen))  # 4
# print(next(gen))  # 9

# ## Generator vs List
# # Using List:
# def square_list(n):
#     result = []
#     for i in range(n):
#         result.append(i * i)
#     return result
# print(square_list(5))
# # Output: [0, 1, 4, 9, 16]

# # Using Generator:
# def square_gen(n):
#     for i in range(n):
#         yield i * i
# for val in square_gen(5):
#     print(val)

# def square_gen(n):
#     for i in range(n):
#         yield i * i
# for val in square_gen(5):
#     print(val)

# def my_gen():
#     print("Start")
#     yield 1     # pauses here after yielding 1
#     print("Middle")
#     yield 2     # pauses here after yielding 2
#     print("End")
#     yield 3     # pauses here after yielding 3
# gen = my_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# # timeline diagram or animation steps
# def clock(n):
#     print("hey")
#     while n>0:
#         print('first')
#         yield n
#         print("second")
#         n=n-1
#         print("third")
# c=clock(4)
# print(next(c))
# print()
# print(next(c))
# print()
# print(next(c))
# print()
# for i in c:
#     print(i)

