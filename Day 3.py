
# nums = range(1,21)

# squares = [n**2 if n % 2 == 1 else n**3 for n in nums if n % 5 != 0]

# squares = []

# for n in nums:
#     if n % 5 == 0:
#         continue
#     if n % 2 == 1:
#         squares.append(n**2)
#     else:
#         squares.append(n**3)

# squares = {}
# for n in nums:
#     squares[n] = n**2

# squares = {n: n**2 for n in nums}

# print(squares)


# student_dict = {
#     "student1": {
#         "name": "Alice",
#         "age": 20,
#         "courses": ["Math", "Science"]
#     },
#     "student2": {
#         "name": "Bob",
#         "age": 22,
#         "courses": ["History", "Art"]
#     }
# }

# young_students = [v for k, v in student_dict.items() if v["age"] < 21]

# # for student_id, student_data in student_dict.items():
# #     if student_data["age"] < 21:
# #         young_students[student_id] = student_data

# print(young_students)


# people_names = ["Alice", "Bob", "Charlie", "David",['hello','hi']]

# test_data = people_names.copy()
# # print(test_data)
# test_data[4][1] = 'Thank you'

# print(test_data)
# print(people_names)

# import copy
# people_names = ["Alice", "Bob", "Charlie", "David",['hello','hi']]
# test_data = copy.deepcopy(people_names)
# test_data[4][1] = 'Thank you'
# print(test_data)
# print(people_names)

# nums_list = range(1, 21)
# sum = 0
# for i in nums_list:
#     sum += i
#     # print(i, sum)
#     if sum > 50:
#         # print("Sum exceeded 50 at number", i)
#         break

# print(sum - 50)

# def square(n):
#     return n**2

# print(square(5))
# print(square(10))
# print(square(15))


# def summation(a, b, c = 0):
#     return a + b + c

# def multiply(a,b,c=1):
#     return a * b * c

# print(multiply(2,3))
# print(multiply(2,3,4))

# def multiply(a,b,c=None):
#     if c is None:
#         return (a*b)
#     else:
#         return (a*b*c)

# print(multiply(2,3))

# def custom_print(value, name=''):
#     if name:
#         print(f"{name} is saying: {value}")
#     else:
#         print(f"hritik is saying: {value}")

# custom_print("Today is a good day")

# def login(username, password, host='localhost', port=8080, database='Attendence', table='Users'):
#     if username == "admin" and password == "password123":
#         return f"login successful into {database}.{table} at {host}:{port}"
#     else:
#         return "login failed, please check your credentials"

# print(login("admin", password= "password123",table='Students', database='SchoolDB'))

# def summation(*args):
#     total = 0
#     for num in args:
#         num = int(num)
#         total += num
#     return total

# print(summation(1,2,3))
# print(summation(10,20,'30','40'))
# print(summation())

# def division(a, b):
#     if b == 0 || a==0:
#         print("Cannot divide by zero")
#     else:
#         print("Division result:", a / b)

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# division(a, b)


# def division(a,b):
#     if b==0:
#         return "undefined because denominator is zero and division by zero is undefined"
#     return a/b

# print(division(10,0))


# def divide(a=None , b=None):
#     if a is not None and b is not None:
#         if b != 0:
#             return a/b
#         else:
#             return ("enter non zero denominator")
#     else:
#         return ("both numerator and denominator are required for division")
            
# div=divide(0)
# print(div)

# def test_function(name, **info):
#     print("Name:", name)
#     print(info)

# test_function("Alice", age=30, city="New York")

# def create_user(name, age, *hobbies, **additional_info):
#     if additional_info.get("profession") == "Engineer":
#         additional_info["done_engineering"] = True

#     user = {
#         "name": name,
#         "age": age,
#         "hobbies": hobbies
#     }
#     user.update(additional_info)
#     return user

# print(create_user("Alice", 30, "Reading", "Traveling", "Cooking",
#              city="New York", profession="Doctor"))


# def factorial(n):
#     return n*factorial(n-1) if n > 1 else 1

# print(factorial(5))  # Output: 120

