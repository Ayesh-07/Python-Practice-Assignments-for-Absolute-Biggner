# -*- coding: utf-8 -*-
"""Assignment # 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T1FEwdE5OokogclKavC6zvlHjtt0BZI4
"""

# 1. Write a program to find the maximum between two numbers.

a = 10
b = 2
if (a > b ):
   print ("a is the maximum")
else:
   print("b is the maximum")

#2. Write a program to find the maximum between three numbers.
a = 88
b = 99
c = 79
if (a > b ):
   print ("a is the maximum")
elif (b > c):
     print("b is the maximum")
else:
     print("c is the maximum")

#3. Write a program to check whether a number is negative, positive or zero.

num = float(input("Enter a number: "))
if num < 0:
    print("The number is negative.")
elif num > 0:
    print("The number is positive.")
else:
    print("The number is zero.")

# 4. Write a program to check whether a number is divisible by 5 and 11 or not.

num = int(input("Enter a number: "))
if (num % 5 == 0):
    print("This number is divisible by 5 ")
elif (num % 11 == 0):
    print("This number is divisible by 11 ")
else:
      print("This number is not divisible by 5 and 11 ")

# 5. Write a program to check whether a number is even or odd.

num = int(input("Enter a number: "))
if (num % 2 == 0):
    print(f"{num} number is even ")
else:
      print(f"{num} number is odd")

# 6. Write a program to check whether a year is leaping year or not.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 7. Write a program to input any alphabet and check whether it is vowel or consonant.


alphabet = input("Enter an alphabet: ")

if len(alphabet) == 1 and alphabet.isalpha():

    alphabet = alphabet.lower()

    if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u':

        print(f"{alphabet} is a vowel.")
    else:
        print(f"{alphabet} is a consonant.")
else:
    print("Please enter a single alphabet.")

# 8. Write a program to check whether a character is uppercase or lowercase alphabet.


alphabet = input("Enter an alphabet: ")
if len(alphabet) == 1 and alphabet.isalpha():

   if alphabet.isupper():
      print ( f"{alphabet} alphabet is uppercase alphabet")
   else:
      print ( f"{alphabet} alphabet is lowercase alphabet")
else:
    print("Please enter a single alphabet.")

# 9. Write a program to input the week number and print weekday.

week_number = int(input("Enter the week number (1-7): "))


if week_number == 1:
    print("Monday")
elif week_number == 2:
    print("Tuesday")
elif week_number == 3:
    print("Wednesday")
elif week_number == 4:
    print("Thursday")
elif week_number == 5:
    print("Friday")
elif week_number == 6:
    print("Saturday")
elif week_number == 7:
    print("Sunday")
else:
    print("Invalid week number. Please enter a number between 1 and 7.")

# 10. Write a program to input the month number and print the number of days in that month.

month = int(input("Enter the month number (1-12): "))

if month >= 1 and month <= 12:

    if month in [1, 3, 5, 7, 8, 10, 12]:
        print("Number of days: 31")
    elif month == 2:
        print("Number of days: 28 or 29")  # Assuming not a leap year
    else:
        print("Number of days: 30")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")

# 11. Write a program to count a minimum number of notes in a given amount.

# 12. Write a program to input marks of five subjects Physics, Chemistry,
# Biology, Mathematics, and Computer. Calculate percentage and grade
# according to the following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F

physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
biology = float(input("Enter Biology marks: "))
mathematics = float(input("Enter Mathematics marks: "))
computer = float(input("Enter Computer marks: "))

# Calculate total marks and percentage
total_marks = physics + chemistry + biology + mathematics + computer
percentage = (total_marks / 500) * 100

if ( percentage >= 90):
       print ("Grade A")

elif (percentage >= 80 ):
        print("Grade B")
elif (percentage >= 70) :
        print("Grade C")
elif (percentage >= 60):
        print("Grade D")
else:
        print("Grade E and F")