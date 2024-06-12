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

# two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
# print(type(two_digit_number))
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number [1])
# two_digit_number = first_digit + second_digit
# print(two_digit_number)



# 3 + 5 addition
# 7 - 3 subtraction
# 3 * 2 multiple
# print(type(6 / 3)) division
#  5 ** 6,  5 to the power of 6, 5*5*5*5*5*5
# P E M D A S
# ()
# **
# * /
# + -

print(3 * 3 + 3 / 3 - 3) 
#  = 7 (3*3) + (3/3) - 3 = 7
#  to get the number 3
print(3 * (3 + 3) / 3 - 3)



# Lesson 2
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# BMI Wikipedia Page

# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):


# NOTE: You should convert the bmi to a whole number and print out a whole number in order to pass all the tests. See examples below.

# 1st input: enter height in meters e.g: 1.65
# height = input()
# 2nd input: enter weight in kilograms e.g: 72
# weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# weight_as_int = int(weight)
# height_as_float = float(height)
# bmi = weight_as_int / height_as_float ** 2
# # or
# bmi = weight_as_int / (height_as_float * height_as_float)
# bmi_as_int = int(bmi)
# print(bmi_as_int)



# Round function
print(round(8/3))
#  Or
print(round(2.666666666, 2))

# // - floor division
print(8//3) 

# Variable
result = 4/2
result /=2
print(result)

score = 0

# User scores a point
score += 1
print(score)


# F-string
print('your score is' + str(score))
#  Better way
score = 0
height = 1.8
isWinning = True
print(f'your score is {score}, your height is {height}, your are winning is {isWinning}')



# Lesson 3
#  was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56
# Example Output
# You have 1768 weeks left.

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
years = 90 - int(age)
weeks = years * 52
print(f'You have {weeks} weeks left.')



