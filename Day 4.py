
# list_of_numbers = [1, 2, [3, 4, 5]]  # [add of int 1, add of int 2, add of a list with int 3,4,5]

# # copied_list = list_of_numbers.copy() # [add of int 1, add of int 2, add of a list with int 3,4,5]

# # copied_list[2][1] = 6

# # print(copied_list)

# # print(list_of_numbers)

# import copy

# new_copied_list = copy.deepcopy(list_of_numbers)

# new_copied_list[2][1] = 6

# print(new_copied_list)

# print(list_of_numbers)



# def update(lst, value):
#     lst = list(lst)+[value]

#     lst.append(value)
#     return lst

# updated_list = update((1, 2, 3), 4)

# print(updated_list)  # Output: [1, 2, 3, 4]

# list_of_numbers = [[1, 2], [3, 4, 5]]

# for sublist in list_of_numbers:
#     print(sublist[2:3])


# list_of_numbers = [x for x in range(1,6)]

# # steps 1 to 10

# squares = []
# for i in list_of_numbers:
#     squares.append(i**2)
#     if i == 3:
#         break

# cubes = []
# for i in list_of_numbers:
#     cubes.append(i**3)

# print(squares)
# print(cubes)
# # steps 10 to 100