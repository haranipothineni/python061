######### If statements
###Q1 Write a Python program to check whether a given number is positive. If the number is positive, print "Positive Number".
# number = float(input("Enter a number: "))
# if number > 0:
#     print("Positive Number")

###Q2 Write a Python program to check whether a given string is empty. If it is empty, print "String is Empty".
# string = input("Enter a string: ")
# if not string:
#     print("String is Empty")

###Q3 Write a Python program to determine whether a given number is positive, negative, or zero using only if statements.
# number = float(input("Enter a number: "))
# if number > 0:
#     print("Positive Number")
# if number < 0:
#     print("Negative Number")
# if number == 0:
#     print("Zero")

###Q4 Write a Python program to check whether a given number is divisible by both 3 and 5. If yes, print "Multiple of 3 and 5".
# number = int(input("Enter a number: "))
# if number % 3 == 0 and number % 5 == 0:
#     print("Multiple of 3 and 5")

###Q5 Write a Python program to check whether a given number is a perfect square. If it is, print "Perfect Square".
# number = int(input("Enter a number: "))
# if number >= 0:
#     root = int(number ** 0.5)
#     if root * root == number:
#         print("Perfect Square")

###Q6 Write a Python program to check whether a given number is divisible by both 2 and 3.
# number = int(input("Enter a number: "))
# if number % 2 == 0 and number % 3 == 0:
#     print("Divisible by both 2 and 3")

###Q7 Write a Python program to check whether a given number is a perfect cube. If it is, print "Perfect Cube".
# number = int(input("Enter a number: "))
# if number >= 0:
#     root = int(round(number ** (1/3)))
#     if root ** 3 == number:
#         print("Perfect Cube")

###Q8 Write a Python program to check whether a given number is a multiple of 4.
# number = int(input("Enter a number: "))
# if number % 4 == 0:
#     print("Multiple of 4")    

#########if-else statements
###Q1 Write a Python program to check whether a given year is a leap year.
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

###Q2 Write a Python program to check whether a given character is a vowel or a consonant.
# char = input("Enter a character: ")
# if char.lower() in ['a', 'e', 'i', 'o', 'u']:
#     print(f"{char} is a vowel.")
# else:
#     print(f"{char} is a consonant.")

###Q3 Write a Python program to check whether a given year is a century year.
# year = int(input("Enter a year: "))
# if year % 100 == 0:
#     print(f"{year} is a century year.")
# else:
#     print(f"{year} is not a century year.")

###Q4 Write a Python program to check whether a given number is a prime number.only if-else statements
# number = int(input("Enter a number: "))
# if number > 1:
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             print(f"{number} is not a prime number.")
#             break
#     else:
#         print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

###Q5 Write a Python program to check whether a person is eligible to vote based on age.
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

###Q6 Write a Python program to check whether a given number is positive or non-positive.
# number = float(input("Enter a number: "))
# if number > 0:
#     print("Positive Number")
# else:
#     print("Non-positive Number")

###Q7 Write a Python program to compare two numbers and print the larger number.
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# if num1 > num2:
#     print(f"{num1} is larger than {num2}.")
# else:
#     print(f"{num2} is larger than {num1}.")

###Q8 Write a Python program to check whether a given character is an alphabet letter or not.
# char = input("Enter a character: ")
# if char.isalpha():
#     print(f"{char} is an alphabet letter.")
# else:
#     print(f"{char} is not an alphabet letter.")

###Q9 Write a Python program to find the smallest among three given numbers without using any built-in functions.
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# if num1 <= num2 and num1 <= num3:
#     smallest = num1
# elif num2 <= num1 and num2 <= num3:
#     smallest = num2
# else:
#     smallest = num3
# print(f"The smallest number is: {smallest}")

###Q10 Write a Python program to check whether a given string is a palindrome.
# string = input("Enter a string: ")
# if string == string[::-1]:
#     print(f"{string} is a palindrome.")
# else:
#     print(f"{string} is not a palindrome.")

###Q11 Write a Python program to find the largest among four given numbers.
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# num4 = float(input("Enter the fourth number: "))
# if num1 >= num2 and num1 >= num3 and num1 >= num4:
#     largest = num1
# elif num2 >= num1 and num2 >= num3 and num2 >= num4:
#     largest = num2
# elif num3 >= num1 and num3 >= num2 and num3 >= num4:
#     largest = num3
# else:
#     largest = num4
# print(f"The largest number is: {largest}")

###Q12 Write a Python program to take two numbers, find their difference, and determine whether the result is positive, negative, or zero.
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# difference = num1 - num2
# if difference > 0:
#     print(f"The difference is positive: {difference}")
# elif difference < 0:
#     print(f"The difference is negative: {difference}")
# else:
#     print("The difference is zero.")

###Q13 Write a Python program to check whether a given year is a leap year using nested if statements.
# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year.")
#     else:
#         print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

###Q14 Write a Python program to check whether a given number is a multiple of 7.
# number = int(input("Enter a number: "))
# if number % 7 == 0:
#     print(f"{number} is a multiple of 7.")    

###Q15 Write a Python program to find the absolute value of a given number without using any built-in functions.
# number = float(input("Enter a number: "))
# if number < 0:
#     absolute_value = -number
# else:
#     absolute_value = number
# print(f"The absolute value is: {absolute_value}")

####### IF-ELIF-ELSE STATEMENT
###Q1 Write a Python program that converts a temperature in Celsius to Fahrenheit or Fahrenheit to Celsius based on user input.
# conversion = input("Enter conversion: ")
# temperature = float(input("Enter temperature: "))
# if conversion == "C to F":
#     fahrenheit = (temperature * 9/5) + 32
#     print(f"Temperature in Fahrenheit: {fahrenheit:.1f}")
# elif conversion == "F to C":
#     celsius = (temperature - 32) * 5/9
#     print(f"Temperature in Celsius: {celsius:.1f}")
# else:
#     print("Invalid conversion type. Please enter 'C to F' or 'F to C'.")

###Q2 Write a Python program that performs addition, subtraction, multiplication, or division based on the user's choice.
# n1=float(input("Enter the first num:"))
# n2=float(input("enter the 2nd num:"))
# o=input("enter operation(+,-,*,/):")
# if o=="+":
#     r=n1+n2
# elif o=="-":
#     r=n1-n2
# elif o=="*":
#     r=n1*n2
# elif o=="/":
#     if n2 == 0:
#         print("Error: Division by zero is not allowed.")
#         pass
#     r=n1/n2
# else:
#     print("invalid operation")
# print("Result:",r)

###Q3 Write a Python program for a simple "Guess the Number" game. Generate a random number and let the user guess it.
# import random
# s= random.randint(1, 10)
# g = int(input("Guess the number: "))
# if g == s:
#     print("Congratulations! You guessed the number.")
# else:
#     print("Wrong guess. Try again.")

###Q4 Write a Python program that checks the strength of a user's password based on certain criteria.
# Password = input("Enter your password: ")
# if len(Password) < 8:
#     print("Password is too short. It must be at least 8 characters long.")
# elif not any(char.isdigit() for char in Password):
#     print("Password must contain at least one digit.")
# elif not any(char.isupper() for char in Password):
#     print("Password must contain at least one uppercase letter.")
# elif not any(char.islower() for char in Password):
#     print("Password must contain at least one lowercase letter.")
# else:
#     print("Password is valid.")

###Q5 Write a Python program that calculates the final price after applying a discount based on the purchase amount.
# purchase_amount = float(input("Enter the purchase amount: "))
# if purchase_amount < 100:
#     discount = 0
# elif 100 <= purchase_amount < 500:
#     discount = 0.1 * purchase_amount  
# elif 500 <= purchase_amount < 1000:
#     discount = 0.2 * purchase_amount  
# else:
#     discount = 0.3 * purchase_amount  
# final_price = purchase_amount - discount
# print(f"Final price after discount: {final_price:.2f}") 

###Q6 Write a Python program that simulates an ATM machine, allowing users to check their balance and withdraw money.only using if and else statements.
# balance = 1000.0  # Initial balance
# print("Welcome to the ATM!")
# action = input("Enter 'check' to check balance or 'withdraw' to withdraw money: ")
# if action == "check":
#     print(f"Your current balance is: ${balance:.2f}")
# elif action == "withdraw":
#     amount = float(input("Enter the amount to withdraw: "))
#     if amount <= balance:
#         balance -= amount
#         print(f"Withdrawal successful. Your new balance is: ${balance:.2f}")
#     else:
#         print("Insufficient funds. Withdrawal failed.") 

###Q7 Write a Python program that greets the user differently based on the time of day.
# hour = int(input("Enter hour: "))
# if 5 <= hour < 12:
#     print("Good Morning")
# elif 12 <= hour < 18:
#     print("Good Afternoon")
# elif 18 <= hour < 22:
#     print("Good Evening")
# else:
#     print("Good Night")

###Q8 Write a Python program that calculates the final price after applying a discount based on a coupon code.
# original_price = float(input("Enter the original price: "))
# coupon_code = input("Enter the coupon code: ")
# if coupon_code == "DISCOUNT10":
#     discount = 0.1 * original_price
# elif coupon_code == "DISCOUNT20":
#     discount = 0.2 * original_price
# elif coupon_code == "DISCOUNT30":
#     discount = 0.3 * original_price
# else:
#     discount = 0
# final_price = original_price - discount
# print(f"Final price after discount: ${final_price:.2f}") 


###Q9 Write a Python program that calculates and prints the grade based on a given score and validates the score.
# score = float(input("Enter the score: "))
# if score < 0 or score > 100:
#     print("Invalid score. Please enter a score between 0 and 100.")
# else:
#     if score >= 90:
#         grade = "A"
#     elif score >= 80:
#         grade = "B"
#     elif score >= 70:
#         grade = "C"
#     elif score >= 60:
#         grade = "D"
#     else:
#         grade = "F"
#     print(f"Grade: {grade}")

###Q10 Write a Python program that acts as a calculator and allows the user to choose addition, subtraction, multiplication, or division.
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operation = input("Enter the operation (+, -, *, /): ")
#
# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     result = num1 / num2
# else:
#     result = "Invalid operation"
#
# print(f"Result: {result}")

###Q11 Write a Python program that determines the number of days in a given month.
# month = input("Enter the month (e.g., January, February, etc.): ")
# if month in ["January", "March", "May", "July", "August", "October", "December"]:
#     days = 31
# elif month in ["April", "June", "September", "November"]:
#     days = 30
# elif month == "February":
#     days = 28  # Not accounting for leap years
# else:
#     days = "Invalid month"
# print(f"Number of days in {month}: {days}")   

###Q12 Write a Python program that calculates BMI and categorizes it as underweight, normal weight, overweight, or obese.
# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     category = "Underweight"
# elif 18.5 <= bmi < 24.9:
#     category = "Normal weight"
# elif 25 <= bmi < 29.9:
#     category = "Overweight"
# else:
#     category = "Obese"
# print(f"Your BMI is: {bmi:.2f}. Category: {category}")

###Q13 Write a Python program that converts letter grades A, B, C, D, and F into their equivalent GPA values.
# grade = input("Enter the letter grade (A, B, C, D, or F): ")
# if grade == "A":
#     gpa = 10.0
# elif grade == "B":
#     gpa = 9.0
# elif grade == "C":
#     gpa = 8.0
# elif grade == "D":
#     gpa = 7.0
# elif grade == "E":
#     gpa = 6.0
# elif grade == "F":
#     gpa = 0.0
# else:
#     gpa = "Invalid grade"
# print(f"Equivalent GPA: {gpa}")

##### Nested If Statements 

###Q1 Given x = 10 and y = 5, determine whether x is greater than y. If it is, check whether it is also greater than 15.
# x = 10
# y = 5
# if x > y:
#     print("x is greater than y")
#     if x > 15:
#         print("x is also greater than 15")
#     else:
#         print("x is not greater than 15")
# else:
#     print("x is not greater than y")

###Q2 Write a Python program that takes a grade as input and prints the corresponding letter grade. If the grade is less than 70, also print "You failed."
# grade = float(input("Enter your grade: "))
# if grade >= 90:
#     letter_grade = "A"
# elif grade >= 80:
#     letter_grade = "B"
# elif grade >= 70:
#     letter_grade = "C"
# else:
#     letter_grade = "F"
# print(f"Your letter grade is: {letter_grade}")
# if grade < 70:
#     print("You failed.")

###Q3 Write a Python program to check credit-card eligibility based on age and income.
# age = int(input("Enter your age: "))
# income = float(input("Enter your annual income: "))
# if age >= 18:
#     if income >= 20000:
#         print("You are eligible for a credit card.")
#     else:
#         print("You are not eligible for a credit card due to insufficient income.")
# else:
#     print("You are not eligible for a credit card due to age restrictions.")  

###Q4 Write a Python program to determine whether a number is even or odd. If it is even, check whether it is greater than 10.
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("The number is even.")
#     if number > 10:
#         print("The number is also greater than 10.")
#     else:
#         print("The number is not greater than 10.")   
# else:
#     print("The number is odd.")

###Q5 Write a Python program that calculates a theme-park ticket price based on age and height.
# age = int(input("Enter your age: "))
# height = float(input("Enter your height in meters: "))
# if age < 12:
#     ticket_price = 10.0  # Child ticket price
# elif 12 <= age < 18:
#     ticket_price = 15.0  # Teen ticket price
# else:
#     if height < 1.5:
#         ticket_price = 20.0  # Adult ticket price for shorter individuals
#     else:
#         ticket_price = 25.0  # Adult ticket price for taller individuals
# print(f"Your ticket price is: ${ticket_price:.2f}")

###Q6 Write a Python program for user authentication. Check the username and password and print the appropriate message.
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == "admin":
#     if password == "password123":
#         print("Login successful!")
#     else:
#         print("Incorrect password.")
# else:
#     print("Incorrect username.")  

###Q7 Write a Python program for ordering food. If the user chooses Burger, ask whether they want fries. If they choose Pizza, ask whether they want extra cheese.
# food_choice = input("What would you like to order? (Burger/Pizza): ")
# if food_choice == "Burger":
#     want_fries = input("Would you like fries with your burger? (Yes/No): ")
#     if want_fries == "Yes":
#         print("You have ordered a burger with fries.")
#     else:
#         print("You have ordered a burger without fries.")
# elif food_choice == "Pizza":
#     want_extra_cheese = input("Would you like extra cheese on your pizza? (Yes/No): ")
#     if want_extra_cheese == "Yes":
#         print("You have ordered a pizza with extra cheese.")
#     else:
#         print("You have ordered a pizza without extra cheese.")
# else:
#     print("Invalid choice.")

###Q8 Write a Python program that checks whether a number is positive, negative, or zero. If positive, also check whether it is even or odd.
# number = float(input("Enter a number: "))
# if number > 0:
#     print("The number is positive.")
#     if number % 2 == 0:
#         print("The number is even.")
#     else:
#         print("The number is odd.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")

###Q9 Write a Python program that asks for age and whether the user has a driver's license. Check whether they are eligible to drive.
# age = int(input("Enter your age: "))
# has_license = input("Do you have a driver's license? (Yes/No): ")
# if age >= 18:
#     if has_license == "Yes":
#         print("You are eligible to drive.")
#     else:
#         print("You are not eligible to drive because you do not have a driver's license.")
# else:
#     print("You are not eligible to drive because you are under 18 years old.")    

###Q10 Write a Python program that checks whether a person is eligible to vote based on age and citizenship.
# age = int(input("Enter your age: "))
# citizenship = input("Are you a citizen? (Yes/No): ")
# if age >= 18:
#     if citizenship == "Yes":
#         print("You are eligible to vote.")
#     else:
#         print("You are not eligible to vote because you are not a citizen.")  
# else:
#     print("You are not eligible to vote because you are under 18 years old.")

###Q11 Write a Python program that takes three numbers as input and prints them in ascending order.
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# if num1 <= num2 and num1 <= num3:
#     if num2 <= num3:
#         print(f"Numbers in ascending order: {num1}, {num2}, {num3}")
#     else:
#         print(f"Numbers in ascending order: {num1}, {num3}, {num2}")
# elif num2 <= num1 and num2 <= num3:
#     if num1 <= num3:
#         print(f"Numbers in ascending order: {num2}, {num1}, {num3}")
#     else:
#         print(f"Numbers in ascending order: {num2}, {num3}, {num1}")
# else:
#     if num1 <= num2:
#         print(f"Numbers in ascending order: {num3}, {num1}, {num2}")
#     else:
#         print(f"Numbers in ascending order: {num3}, {num2}, {num1}")  

###Q12 Write a Python program that calculates a discount based on purchase amount and membership status.
# purchase_amount = float(input("Enter the purchase amount: "))
# membership_status = input("Are you a member? (Yes/No): ")
# if membership_status == "Yes":
#     if purchase_amount >= 100:
#         discount = 0.2 * purchase_amount  # 20% discount for members
#     else:
#         discount = 0.1 * purchase_amount  # 10% discount for members
# else:
#     if purchase_amount >= 100:
#         discount = 0.1 * purchase_amount  # 10% discount for non-members
#     else:
#         discount = 0  # No discount for non-members with purchase < 100
# final_price = purchase_amount - discount
# print(f"Final price after discount: ${final_price:.2f}")

###Q13 Write a Python program that classifies a character as a vowel, consonant, or neither.
# char = input("Enter a character: ")
# if len(char) == 1 and char.isalpha():
#     if char.lower() in ['a', 'e', 'i', 'o', 'u']:
#         print(f"{char} is a vowel.")
#     else:
#         print(f"{char} is a consonant.")
# else:
#     print("Invalid input. Please enter a single alphabetic character.")   

###Q14  Write a Python program that recommends books based on the reader's age and genre preference.
# age = int(input("Enter your age: "))
# genre = input("Enter your preferred genre (Fiction/Non-Fiction): ")
# if age < 12:
#     if genre == "Fiction":
#         print("Recommended books: 'Charlotte's Web', 'Harry Potter and the Sorcerer's Stone'")
#     else:
#         print("Recommended books: 'National Geographic Kids', 'The Way Things Work'")
# elif 12 <= age < 18:
#     if genre == "Fiction":
#         print("Recommended books: 'The Hunger Games', 'Percy Jackson & the Olympians'")
#     else:
#         print("Recommended books: 'A Brief History of Time', 'The Immortal Life of Henrietta Lacks'")
# else:
#     if genre == "Fiction":
#         print("Recommended books: 'To Kill a Mockingbird', '1984'")
#     else:
#         print("Recommended books: 'Sapiens: A Brief History of Humankind', 'Educated'")

###Q15 Write a Python program that calculates movie-ticket prices based on age and whether the show is a matinee.
# age = int(input("Enter your age: "))
# is_matinee = input("Is it a matinee show? (Yes/No): ")
# if age < 12:
#     ticket_price = 5.0  # Child ticket price
# elif 12 <= age < 65:
#     if is_matinee == "Yes":
#         ticket_price = 8.0  # Adult matinee ticket price
#     else:
#         ticket_price = 12.0  # Adult regular ticket price
# else:
#     ticket_price = 6.0  # Senior ticket price
# print(f"Your ticket price is: ${ticket_price:.2f}")

###Q16 Write a Python program that calculates delivery charges based on distance and order amount. nested if statements
# distance = float(input("Enter the delivery distance in kilometers: "))
# order_amount = float(input("Enter the order amount: "))
# if distance <= 5:
#     if order_amount >= 50:
#         delivery_charge = 0  # Free delivery for orders above $50 within 5 km
#     else:
#         delivery_charge = 5  # $5 delivery charge for orders below $50 within 5 km
# elif distance <= 10:
#     if order_amount >= 100:
#         delivery_charge = 0  # Free delivery for orders above $100 within 10 km
#     else:
#         delivery_charge = 10  # $10 delivery charge for orders below $100 within 10 km
# else:
#     delivery_charge = 15  # $15 delivery charge for distances above 10 km
# print(f"Delivery charge: ${delivery_charge:.2f}")

###Q17 Write a Python program that classifies an employee's performance based on their score and years of service, then calculates the bonus.
# score = float(input("Enter the employee's performance score (0-100): "))
# years_of_service = int(input("Enter the employee's years of service: "))
# if score >= 90:
#     performance_category = "Excellent"
#     if years_of_service >= 5:
#         bonus = 1000
#     else:
#         bonus = 500
# elif score >= 75:
#     performance_category = "Good"
#     if years_of_service >= 5:
#         bonus = 500
#     else:
#         bonus = 250
# elif score >= 60:
#     performance_category = "Average"
#     if years_of_service >= 5:
#         bonus = 250
#     else:
#         bonus = 100
# else:
#     performance_category = "Poor"
#     bonus = 0
# print(f"Performance Category: {performance_category}")
# print(f"Bonus: ${bonus:.2f}")

###Q18 Write a Python program that calculates the late fee for a borrowed book based on overdue days and book type.
# overdue_days = int(input("Enter the number of overdue days: "))
# book_type = input("Enter the book type (Regular/Reference): ")
# if overdue_days > 0:
#     if book_type == "Regular":
#         late_fee = overdue_days * 0.5  # $0.50 per day for regular books
#     elif book_type == "Reference":
#         late_fee = overdue_days * 1.0  # $1.00 per day for reference books
#     else:
#         late_fee = 0
#         print("Invalid book type. Please enter 'Regular' or 'Reference'.")
# else:
#     late_fee = 0
# print(f"Late fee: ${late_fee:.2f}")

###Q19 Write a Python program that checks scholarship eligibility based on GPA and extracurricular activities.
# gpa = float(input("Enter your GPA: "))
# extracurricular_activities = input("Do you participate in extracurricular activities? (Yes/No): ")
# if gpa >= 3.5:
#     if extracurricular_activities == "Yes":
#         print("You are eligible for the scholarship.")
#     else:
#         print("You are not eligible for the scholarship due to lack of extracurricular activities.")
# else:
#     print("You are not eligible for the scholarship due to low GPA.") 

###Q20 Write a Python program that recommends clothing based on temperature and whether it is raining.
# temperature = float(input("Enter the temperature in Celsius: "))
# is_raining = input("Is it raining? (Yes/No): ")
# if temperature < 10:
#     if is_raining == "Yes":
#         print("Wear a heavy coat and carry an umbrella.")
#     else:
#         print("Wear a heavy coat.")
# elif 10 <= temperature < 20:
#     if is_raining == "Yes":
#         print("Wear a light jacket and carry an umbrella.")
#     else:
#         print("Wear a light jacket.")
# elif 20 <= temperature < 30:
#     if is_raining == "Yes":
#         print("Wear a t-shirt and carry an umbrella.")
#     else:
#         print("Wear a t-shirt.")
# else:
#     if is_raining == "Yes":
#         print("Wear shorts and carry an umbrella.")
#     else:
#         print("Wear shorts.")     

###Q21 Write a Python program that recommends a movie based on the user's preferred genre and age group.
# genre = input("Enter your preferred movie genre (Action/Comedy/Drama): ")
# age_group = input("Enter your age group (Child/Teen/Adult): ")
# if genre == "Action":
#     if age_group == "Child":
#         print("Recommended movie: 'The Incredibles'")
#     elif age_group == "Teen":
#         print("Recommended movie: 'The Avengers'")
#     elif age_group == "Adult":
#         print("Recommended movie: 'Mad Max: Fury Road'")
#     else:
#         print("Invalid age group. Please enter 'Child', 'Teen', or 'Adult'.")
# elif genre == "Comedy":
#     if age_group == "Child":
#         print("Recommended movie: 'Despicable Me'")
#     elif age_group == "Teen":
#         print("Recommended movie: 'Superbad'")
#     elif age_group == "Adult":
#         print("Recommended movie: 'The Hangover'")
#     else:
#         print("Invalid age group. Please enter 'Child', 'Teen', or 'Adult'.")
# elif genre == "Drama":
#     if age_group == "Child":
#         print("Recommended movie: 'The Lion King'")
#     elif age_group == "Teen":
#         print("Recommended movie: 'The Fault in Our Stars'")
#     elif age_group == "Adult":
#         print("Recommended movie: 'The Shawshank Redemption'")
#     else:
#         print("Invalid age group. Please enter 'Child', 'Teen', or 'Adult'.")
# else:
#     print("Invalid genre. Please enter 'Action', 'Comedy', or 'Drama'.")  

###Q22  Write a Python program that determines whether a credit-card application is approved based on credit score and income.
# credit_score = int(input("Enter your credit score: "))
# income = float(input("Enter your annual income: "))
# if credit_score >= 700:
#     if income >= 50000:
#         print("Your credit-card application is approved.")
#     else:
#         print("Your credit-card application is not approved due to insufficient income.")
# else:
#     print("Your credit-card application is not approved due to low credit score.")

###Q23 Write a Python program that determines the vehicle registration fee based on vehicle type and emissions status.
# vehicle_type = input("Enter the vehicle type (Car/Truck/Motorcycle): ")
# emissions_status = input("Enter the emissions status (Pass/Fail): ")
# if vehicle_type == "Car":
#     if emissions_status == "Pass":
#         registration_fee = 100
#     else:
#         registration_fee = 150
# elif vehicle_type == "Truck":
#     if emissions_status == "Pass":
#         registration_fee = 150
#     else:
#         registration_fee = 200
# elif vehicle_type == "Motorcycle":
#     if emissions_status == "Pass":
#         registration_fee = 50
#     else:
#         registration_fee = 75
# else:
#     registration_fee = 0
#     print("Invalid vehicle type. Please enter 'Car', 'Truck', or 'Motorcycle'.")
# print(f"Vehicle registration fee: ${registration_fee:.2f}")

