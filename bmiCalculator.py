"""
This is a program to calculate a person's BMI or Body Mass Index

This program is developed by Misbah Ahmed

"""

#taking user input
weight = int(input("Enter weight: "))
height = float(input("Enter height in metre: "))

#calculating the BMI using the formula weight/height^2
bmi = weight / (height * height)

#making desicions
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi < 30:
    print("Overweright")
elif bmi >= 30:
    print("Obesity")
