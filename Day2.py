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

# # print(student_dict.get("student11", {"name": "Student not found"}).get("name"))  # Output: Student not found
# # print(student_dict["student2"]["courses"])  # Output: ['History', 'Art']

# student_dict["student3"] = {
#     "name": "Charlie",
#     "age": 23,
#     "courses": ["Physics", "Chemistry"]
# }

# student_1_data = student_dict.pop("student1")  # This will raise an error because popitem() does not take arguments

# print(student_1_data)
# print(student_dict)

# temp = input("Enter today's temperature in Celsius: ")
# temp = int(temp)

# if temp >= 50:
#     print("It's a too hot a day to go outside")
#     if temp >= 80:
#         print("Stay hydrated! keep dring water again and again")
#     else:
#         print("It's advisable to stay indoors, drink water if necessory")
# elif temp >= 30:
#     print("It's a hot day")
# elif temp >= 10:
#     print("It's a warm day")
# elif temp >= 0:
#     print("It's a cold day")
# else:
#     print("It's chilling outside, stay warm!")

# print("Enjoy your day!")

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


# if student_dict is None:
#     output =  "Student data is not available."
# if student_dict.get("student1") is None:
#     output = "Student not found."
# if student_dict.get("student1").get("age") is None:
#     output = "Age information is missing."
# output = "Student is an adult." if student_dict.get("student1").get("age") > 18 else "Student is a minor."



# if (student_data := student_dict.get("student1")) is not None:
#     if (age := student_data.get("age")) is not None:
#         if age > 18:
#             print("Student is an adult.")
#         else:
#             print("Student is a minor.")
#     else:
#         print("Age information is missing.")
# else:
#     print("Student not found.")


# gender = "Male"
# pronoun = "He" if gender == "Male" else "She" if gender == "Female" else "They"

# if gender == "Male":
#     pronoun = "He"
# elif gender == "Female":
#     pronoun = "She"
# else:
#     pronoun = "They"

# match gender:
#     case "Male":
#         pronoun = "He"
#     case "Female":
#         pronoun = "She"
#     case _:
#         pronoun = "They"

# print(pronoun)  # Output: He

# fruits_list = ["Apple", "Banana", "Cherry", "Date"]

# # output = fruits_list.pop()
# # output = fruits_list.pop()

# # print(output)  # Output: Cherry

# # fruits_list.remove("Banana")
# del(fruits_list[0])

# print(fruits_list[::-2])  # Output: ['Apple', 'Banana', 'Date']


# num = input("Enter a number to count odd number below given number: ")

# num = int(num)

# num_list  = range(1, num)
# counter = 0
# odd_nums_list = []
# for i in num_list:
#     if (i % 2 == 0):
#         continue
#     counter += 1
#     odd_nums_list.append(i)
    
# print("Count of odd numbers below ", num, " is ", counter)
# print("Odd numbers below ", num, " are: ", odd_nums_list)



# counter = 1
# while counter <= num:
#     if counter % 2 == 1:
#         print(counter)
#     counter += 1

# fruits_list = ["Apple", "Banana", "Cherry_box", "Date"]

# cherry_index = 0

# for i in fruits_list:
#     print("checking for cherry at index", cherry_index)
#     current_fruit = i
#     if current_fruit == "Cherry":
#         print("Cherry found at index", cherry_index)
#         break
#     cherry_index += 1
# else:
#     print("Cherry not found in the list")

# print("Loop ended")

