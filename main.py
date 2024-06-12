# Data Types


# Strings
print("Hello"[4])
print('123' + '345')

# Subscript
# H E L L O
# 0 1 2 3 4




# Integer

# larger numbers with a comma
print(123 + 345)
123_456_789



# Float

# has a decimal point
# 3.147


# Boolean
# True or False




# num_char = len(input('What is your name?'))
# print("Your name has " + num_char + " characters.") Wrong can't do

# print(type(num_char))

# Type Casting
# new_num_char = str(num_char)
# print('Your name has ' + new_num_char + ' characters.')

# a = str(123)
a = float(123)

print(type(a))

# print(70 + float('100.5'))
print(str(70) + str(100))


# Lesson 1
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.
# The last line of your program should print the result.
# Example 1 Input
# 39
# Example 1 Output
# 12

two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
print(type(two_digit_number))
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number [1])
two_digit_number = first_digit + second_digit
print(two_digit_number)