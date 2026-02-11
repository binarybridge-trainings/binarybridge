import Day_5

user_input = input("Input a word to check if it is palindrome or not: ")
result = Day_5.is_palindrome(user_input)

if result == True:
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")


from math import sqrt as sqareroot

print(sqareroot(9))