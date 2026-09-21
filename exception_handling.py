# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# try:
#     value = int(input("Enter a number: "))
#     result = 10 / value
# except ValueError:
#     print("Invalid input. Please enter a number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# try:
#     value = int(input("Enter a number: "))
#     result = 10 / value
# except (ValueError, ZeroDivisionError) as e:
#     print(f"An error occurred: {e}")

# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print("Division successful!", result)

# try:
#     file = open("data.txt", "r")
#     data = file.read()
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     print("Execution completed.")
#     file.close()

# value = -10
# if value < 0:
#     raise ValueError("Value cannot be negative.")
# try:
#     raise Exception("Custom error message")
# except Exception as e:
#     print(e)

# class NegativeValueError(Exception):
#     pass
# value = -5
# if value < 0:
#     raise NegativeValueError("Negative values are not allowed.")

# try:
#     try:
#         result = 10 / 0
#     except ZeroDivisionError:
#         print("Handled division by zero inside nested try block.")
# except Exception as e:
#     print(f"Outer exception handler: {e}")

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
# except ValueError:
#     print("Invalid input. Please enter a number.")
# else:
#     print("Result is:", result)
# finally:
#     print("Program finished.")

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print("Result:", a / b)
# except ZeroDivisionError:
#     print("You cannot divide by zero!")

# try: 
#     a = 10
#     b = 0
#     print('Execution start')
#     print(a + b)
#     print(a - b)
#     print(a / b)
#     print(a * b)
#     print(a * b)
# except ZeroDivisionError as e:
#     print("dont divide any number with zero")
#     print("Exception description is:", e)
# print("execution stopped")

# try:
#     age = int(input("Enter your age: "))  # Enter: "abc"
#     print("Your age is", age)
# except ValueError:
#     print("Please enter a valid number!")

# try:
#     nums = [10, 20, 30]
#     print(nums[5])
# except IndexError:
#     print("Index out of range!")

# try:
#     a = int("hello")
# except Exception as e:
#     print("Something went wrong:", e)

# try:
#     data = {"name": "ABCD"}
#     print(data["age"])
# except KeyError:
#     print("Key not found in dictionary!")

