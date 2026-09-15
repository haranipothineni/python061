# def student():
#     name = "Harani"
#     print(name)
# student()
# # Output:
# # Harani

# company = "Codegnan"
# def display():
#     print(company)
# display()
# # Output:
# # Codegnan

# name = "Global Name"
# def display():
#     name = "Local Name"
#     print(name)
# display()
# print(name)
# # Output:
# # Local Name
# # Global Name

# count = 10
# def update():
#     global count
#     count = 20
# update()
# print(count)
# # Output:
# # 20

# def outer():
#     count = 10
#     def inner():
#         nonlocal count
#         count += 5
#     inner()
# print(count)
# outer()
# # Output:
# # 15

#### LEGB Rule
# x = 100
# def outer():
#     x = 50
#     def inner():
#         x = 20
#         print(x)
#     inner()
# outer()
# # Output:
# # 20

# def update(number):
#     number = 100
#     print("Inside Function:", number)
# value = 50
# update(value)
# print("Outside Function:", value)
# # Output:
# # Inside Function: 100
# # Outside Function: 50

# def update(items):
#     items.append("Laptop")
# cart = ["Mobile", "Watch"]
# update(cart)
# print(cart)
# # Output:
# # ['Mobile', 'Watch', 'Laptop']

# def update(profile):
#     profile["city"] = "Hyderabad"
# customer = {"name": "Harani"}
# update(customer)
# print(customer)
# # Output:
# # {'name': 'Harani', 'city': 'Hyderabad'}

##### Recursive Function

## Q1. Write a recursive function to print numbers from 1 to N.
# def pn(n):
#     for i in range(1,n+1):
#         print(i)
# n=int(input())
# pn(n)

## Q2. Write a recursive function to print numbers from N to 1.
# def np(n):
#     for i in range(n,0,-1):
#         print(i)
# n=int(input())
# np(n)

## Q3. Write a recursive function to find the sum of first N natural numbers.
# def sn(n):
#     print((n*(n+1))/2)
# n=int(input())
# sn(n)

## Q4. Write a recursive function to find the product of first N natural numbers.
# def pn(n):
#     p=1
#     for i in range(1,n+1):
#         p=p*i
#     print(p)
# n=int(input())
# pn(n)

## Q5. Write a recursive function to find the factorial of a number. 
# def fn(n):
#     p=1
#     for i in range(n,0,-1):
#         p=p*i
#     print(p)
# n=int(input())
# fn(n)

## Q6. Write a recursive function to calculate x raised to the power n.
# def p(m,n):
#     print(m**n)
# a=int(input())
# b=int(input())
# p(a,b)

## Q7. Write a recursive function to reverse a string.
# def rs(n):
#     print(n[::-1])
# a=input()
# rs(a)

## Q8. Write a recursive function to count the number of characters in a string without using len().
# def cs(n):
#     c=1
#     for i in n:
#         c=c+1
#     print(c)
# n=input()
# cs(n)

## Q9. Write a recursive function to print the following pattern.
# def print_pattern(s, index=0):
#     if index == len(s):
#         return
#     print(s[:index+1])
#     print_pattern(s, index + 1)
# s=input()
# print_pattern(s)

## Q10. Write a recursive function to print the following pattern.
# def print_pattern(s):
#     if len(s) == 0:
#         print(s)
#     print_pattern(s[:-1])
# s=input()
# print_pattern(s)

## Q11. Write a recursive function to print all substrings of length 4.
# def print_substrings(s, start=0):
#     if start + 4 > len(s):
#         return
#     print(s[start:start+4])
#     print_substrings(s, start + 1)
# s=input()
# print_substrings(s)

## Q12. Write a recursive function to find the sum of digits of a number.
# def ss(n):
#     s=0
#     for i in n:
#         s=s+int(i)
#     print(s)
# a=input()
# ss(a)

## Q13. Write a recursive function to find the product of digits of a number.
# def ps(n):
#     s=1
#     for i in n:
#         s=s*int(i)
#     print(s)
# a=input()
# ps(a)

## Q14. Write a recursive function to count vowels in a string.
# def count_vowels(s):
#     if s == "":
#         return 0
#     if s[0] in "aeiouAEIOU":
#         return 1 + count_vowels(s[1:])
#     else:
#         return count_vowels(s[1:])
# a=input()
# print(count_vowels(a))

## Q15. Write a recursive function to check whether a string is a palindrome.
# def sp(n):
#     if n[::-1]==n:
#         print("palindrome")
#     else:
#         print("not palindrome")
# a=input()
# sp(a)
