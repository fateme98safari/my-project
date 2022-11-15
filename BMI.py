import math
w = float(input("please enter your weight (kg): "))
h = float(input("please enter your height(m): "))
BMI = w / (h * h)
if BMI < 18.5:
    print("you are underweight")
elif 18.5 < BMI < 24.9:
    print("you are normal weight")
elif 25 < BMI < 29.9:
    print("you are over weight")
elif 30 < BMI < 34.9:
    print("you are obeslty")
elif 35 < BMI < 39.9:
    print("you are extreme obeslty")





