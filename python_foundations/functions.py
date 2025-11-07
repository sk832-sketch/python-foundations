# To define a function in Python, we use the def keyword, followed by the function's name, parentheses (), and a colon : 
# Inside the parentheses, you can specify arguments (inputs the function can accept). The code inside the function is indented.
# def greet():
#     print("Hello, world!")
# greet()

# Arguments are values you pass into the function to make it work with specific data. For example, if you want the greet function to greet a specific person, you could add an argument called 'name'.
# def greet(name):
#     print(f"Hello, {name}!")
# greet("John")

# You can also add multiple arguments to a function. For example, if you want the greet function to greet a specific person and say hello in a specific language, you could add two arguments called name and language.
# def greet(name, language):
#     if language == "English":
#         print(f"Hello, {name}!")
#     elif language == "Spanish":
#         print(f"Hola, {name}!")
#     else:
#         print(f"Hello, {name}!")
# greet("John", "English")

# def add_numbers(a, b):
#     result = a + b
#     print(result)

# add_numbers(1, 2)

# Practice - Define an argument that calculates the total bill including tips and evenly distributes amongst people.
# def calculate_total (bill_amount, tip_percentage, people):
#     total_bill = bill_amount + (tip_percentage/100)*bill_amount
#     per_person = total_bill/people
#     print(per_person)
#     return total_bill # We can also use 'return' to store the value of the argument and use later.

# calculate_total(80, 20, 3)

# You can also set default values for arguments. If an argument with a default value is not provided, Python will use the default. 
# This can make functions more flexible.
# def greet(name="stranger"):
#     print("Hello, " + name + "!")
# If you call greet() without an argument it will return 'stranger' as the name.

# Practice - Define an argument that takes the total bill, tip percentage, taxes and then 
# proportionately divides it based on how much a person spent.
# Variables needed: person_spent, tips, taxes, total_bill.
# person_spent = meal_amount + meal_amount/total_bill * tip + meal_amount/total_bill * taxes

def tip (meal_amount, total_bill, tip):
    result = (meal_amount/total_bill) * tip
    return result

def taxes (meal_amount, total_bill, taxes):
    result = (meal_amount/total_bill) * taxes
    return result

person_spent = 25 + tip(25, 100, 20) + taxes(25, 100, 10)
print(person_spent)

