
s1=int(input("please enter  the first side of triangle: "))
s2=int(input("please enter  the secound side of triangle: "))
s3=int(input("please enter  the third side of triangle: "))
a = s1 + s2
b = s1 + s3
c = s2 + s3
if s3 < a and  s2 < b and  s1 < c:
    print("this triangle is exist")
else:
    print("this triangle is not exist")