import math
name = input("please enter name: ")
family = input("please enter family: ")
s1 = float(input("enter the first score: "))
s2 = float(input("enter the secound score: "))
s3 = float(input("enter the third score: "))
ave = (s1 + s2 + s3) / 3
if ave < 12:
    print("your status is Fail")
elif 12 < ave < 17:
     print("your status is Normal")
elif ave > 17:
     print("your status is Great")

