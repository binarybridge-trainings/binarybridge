def is_palindrome(word: str) -> bool:
    if word == word[::-1]:
        return True
    else:
        return False
    

if __name__ == "__main__":
    user_input = input("Input a word to check if it is palindrome or not: ")
    result = is_palindrome(user_input)

    if result == True:
        print(user_input, "is a palindrome")
    else:
        print(user_input, "is not a palindrome")



# # Generator function creation 
# def multiples(n: int):
#     multiples = []
#     for i in range(1, 11):
#         multiples.append(i * n)
#     return multiples

# result_5 = multiples(5)

# for i in result_5:
#     print(i)

# result_10 = multiples(10)

# for i in result_10:
#     print(i)

# print(result_5)


# def multiples_generator(n: int) :

#     for i in range(1, 11):
#         print(f" {i} * {n} = {i*n}")
#         yield

# result_5_gen = multiples_generator(5)


# for i in result_5_gen:
#     print(" ", end='')

# print(result_5_gen)

# strings quotations and f-strings
# string_1 = "chaithanya's!" \
# "great day to learn python"

# string_2 = 'Hello, World!'

# string_3 = """Hello, World! 
# This is a multi-line string.
# It can span multiple lines without the need for escape characters.
# You can include both single's and double"s quotes without any issues."""

# string_4 = ''''"Hello, World!"' 
# This is a multi-line string.
# It can span multiple lines without the need for escape characters.
# You can include both single and double quotes without any issues.'''

# string_5 = "hello's" + '" world!"'

# print(string_5)


# def greet(name):
#     return f"Hello {name} {5+5}"

# print(greet("Chaithanya"))


# for fruit in ['a','a','a','a','a','a','a','a','a','a', 
#               'a','a','a','a','a','a','a',
#               'a','a','a','a','a','a','a']:
#     print(fruit)



# # typehints
# from typing import List, Dict, Optional

# # # Generator function creation 
# def multiples(n: int) -> List[int]:
#     multiples = []
#     for i in range(1, 11):
#         multiples.append(i * n)
#     return multiples

# def sqauared_dictonary(n: int) -> Dict[int, int]:
#     return {i : i**2 for i in range(1,n+1)}


# def summation(a: int,b : int,*c : int) -> Optional[int]:
#     if a == b == 0:
#         return None
#     return a+b+sum(c)

# print(summation(1,2,12,1))

# input = 5
# def double_number(number: int | float) -> int | float:
#     return int(number) * 2

# print(double_number(input))


# import argparse

# # 1. Create the parser (The container)
# parser = argparse.ArgumentParser(description="A tool to greet users.")

# # 2. Add arguments (The rules)
# parser.add_argument("name")
# parser.add_argument("--age", type=int, default=None, help="Number of year to vote")

# # 3. Parse arguments (The execution)
# args = parser.parse_args()

# if args.age is None:
#     age = int(input("Please enter your age : "))
# else:
#     age = args.age

# if age>=18:
#     output = f"Hello, {args.name}! you are allowed" 
# else:
#     output = f"Hello, {args.name}! you are allowed after {18-age} years"

# print(output)


