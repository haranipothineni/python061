### For Loop

# numbers = [10, 20, 30, 40]
# for i in numbers:
#     print(i)

# l = [1, 2, 3, 4]
# i = iter(l)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# r = range(1, 10)
# print(r)

# r = range(1, 10)
# l = list(r)
# print(l)

# range(10)

# r = range(10)
# print(list(r))

# for i in range(1, 6):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# range(1, 6)
# range(1, 11, 2)
# range(1, 20, 3)
# range(10, 0, -1)

## Even Numbers
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

### while loop

##Q1 Reverse a Number
# n = int(input("Enter n value: "))
# original = n
# rev = 0
# while n > 0:
#     r = n % 10
#     rev = rev * 10 + r
#     n = n // 10
# print(f"The reverse of {original} is:", rev)

##Q2 Check Whether a Number is Palindrome
# n = int(input("Enter number: "))
# original = n
# rev = 0
# while n > 0:
#     r = n % 10
#     rev = rev * 10 + r
#     n = n // 10
# if original == rev:
#     print("Given number is palindrome")
# else:
#     print("Given number is not palindrome")

##Q3 Palindrome Using String
# n = 124
# s = str(n)
# if s == s[::-1]:
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")

##Q4 Count Even Digits in a Number
# n = 123456
# s = str(n)
# c = 0
# for i in s:
#     if int(i) % 2 == 0:
#         c = c + 1
# print("Count of even digits:", c)

##Q5 Factors of a Number
# n = int(input("Enter number: "))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)

##Q6 Count Number of Factors
# n = int(input("Enter number: "))
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count = count + 1
# print("Number of factors:", count)

##Q7 Factorial of a Number
# n = int(input("Enter number: "))
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
# print("Factorial:", fact)

##Q8 Armstrong Number
# n = int(input("Enter number: "))
# original = n
# total = 0
# while n > 0:
#     r = n % 10
#     total = total + r ** 3
#     n = n // 10
# if original == total:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")
