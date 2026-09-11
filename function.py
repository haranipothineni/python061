# def Add(a, b):
#     print(a + b)
# Add(10, 20)
# Add(100, 200)
# Add(50, 30)

def calculate_total(price, quantity):
    print(price * quantity)
calculate_total(100, 2)
calculate_total(250, 4)

# User Defined Function
def Greet():
    print("Welcome to Python")
Greet()

def show_welcome():
    print("Welcome to ABC Bank")
show_welcome()

def Greet(name, age):
    print(f"My name is {name}")
    print(f"My age is {age}")
Greet("Harani", 23)

def student_details(name, course):
    print(name, course)
student_details("Harani", "Python")

def Add(a, b):
    c = a + b
    return c
result = Add(10, 20)
print(result)

def Greet(name, age):
    print(f"My name is {name} and age is {age}")
Greet(name="Harani", age=23)

Greet(age=23, name="Harish")

def CountryDetails(country="India"):
    print("My country is:", country)
CountryDetails("USA")
CountryDetails()

def ItemBillCal(*items):
    print(items)
ItemBillCal(10, 20, 30)
ItemBillCal(10, 20, 30, 40, 50, 60)

def ItemBillCal(*items):
    print(type(items))

def ItemBillCal(*items):
    print("All items:", items)
    print("Total:", sum(items))
ItemBillCal(100, 200, 300, 400)

def ItemBillCal(a, b, *items):
    print("First item:", a)
    print("Second item:", b)
    print("Remaining items:", items)
ItemBillCal(10, 20, 30, 40, 50)

def UserInfo(**details):
    print(details)
UserInfo(name="Raju", age=23, height=5.7)

def UserInfo(**details):
    print(details["name"])
    print(details["age"])
UserInfo(name="Raju", age=23)

def UserInfo(color, **details):
    print("Color:", color)
    print("Details:", details)
UserInfo(
    color="Black",
    name="Raju",
    age=23,
    height=5.7
)

def User(name, age, /):
    print(name, age)
User("Harani", 21)

def User(*, name, age):
    print(name, age)
User(name="Harani", age=21)

def Student(name, /, age, *, course):
    print(name, age, course)
Student("Harani", 22, course="Python")


# Practice
def calculate_total(m1, m2, m3):
    return m1 + m2 + m3
total = calculate_total(80, 75, 90)
print("Total:", total)

def calculate_average(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return average
result = calculate_average(80, 70, 90)
print("Average:", result)

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = check_even_odd(10)
print(result)

def calculate_discount(amount):
    if amount >= 5000:
        discount = amount * 0.20
    elif amount >= 2000:
        discount = amount * 0.10
    else:
        discount = 0
    return discount
discount = calculate_discount(6000)
print("Discount:", discount)

def calculate_bill(price, quantity):
    total = price * quantity
    if total >= 5000:
        discount = total * 0.20
    else:
        discount = 0
    final_amount = total - discount
    return final_amount
bill = calculate_bill(1000, 6)
print("Final Bill:", bill)

def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Invalid username or password"
result = login("admin", "1234")
print(result)

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
x, y = calculate(20, 10)
print("Addition:", x)
print("Subtraction:", y)

def Add(a, b):
    return a + b
def Display():
    result = Add(10, 20)
    print("Result:", result)
Display()

