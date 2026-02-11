# Core - math, os, sys, json

# Core functions - print, input, len, range
# Optional functions - json.load, os.path.join, timedata


# Optional - requests, tesorflow, numpy

# age = 8
# height = 1.35
# name = 'chaithanya'
# is_student = True
# spare_variable = None

# print(type(age))
# print(type(height))
# print(type(name))
# print(type(is_student))
# print(type(spare_variable))

# input_value = input("Input you age : ")
# print("Your age next year will be : ", end="")
# print(int(input_value) + 1)

# print(int(5))
# print(int("5"))
# print(int(5.8))
# # print(int("five"))
# print(int(True))
# print(int(False))
# # print(int(None))

# print(float(5))
# print(float("5.8"))
# print(float(5.8))
# # print(float("five.point.eight"))
# print(float(True))
# print(float(False))


# print(str(5))
# print(str(5.8))
# print(str(True))
# print(str(False))
# print(str(None))

# print(bool(5))
# print(bool(0))
# print(bool(5.8))
# print(bool(0.0))
# print(bool("Hello"))
# print(bool(""))
# print(bool(None))

# Operators - [[+, -, *, /, %, //, **, +=, -=, ==, !=, >, <, >=, <=, and, or, not]]
# print(27 ** (1/3))

# num_1 = 10
# num_2 = 3

# num_1 += 2
# num_1 /= 6 
# num_1 += 1
# print(num_1)

# print(num_1 is num_2)

# bool_1 = True
# bool_2 = False

# print(not bool_2)
# print(bool_1 or bool_2)


# collecctions - list, tuple, set, dict

# list : mutable, ordered, allows duplicates, heterogeneous
# tuple : immutable, ordered, allows duplicates, heterogeneous

# fruits_list = ['apple', 'banana', 'cherry', 'pineapple','apple',1,2,0,'23',3.5,True]
# fruits_list.append('orange')
# # fruits_list.remove('banana')
# # fruits_list[1] = 'blueberry'
# last_fruit = fruits_list.pop()
# last_fruit = fruits_list.pop()
# last_fruit = fruits_list.pop()
# print(fruits_list)
# print(last_fruit)

# fruits_tuple = ('apple', 'banana')

# fruits_list = list(fruits_tuple)
# fruits_list.append('orange')
# fruits_tuple = tuple(fruits_list)

# print(fruits_tuple)



# # Indexing and Slicing
# print(fruits_list[0])
# print(fruits_list[1])
# print(fruits_list[-1])
# print(fruits_list[-2])

# print(fruits_tuple)

# #Set : mutable, unordered, no duplicates, heterogeneous
# fruits_set = {'apple', 'banana', 'cherry', 'pineapple','apple'}
# fruits_set.add('orange')
# fruits_set.remove('banana')

# print(fruits_set)


# #Dict : mutable, unordered, no duplicates(keys), heterogeneous
student_dict = {
    'name' : 'chaithanya',
    'age' : 8,
    'is_student' : True,
    'marks' : [85, 90, 78]
}

