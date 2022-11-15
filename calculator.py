import math
result = 0
r = 0
print("please select")
print("+:sum")
print("-:sub")
print("*:mul")
print("/:div")
print("sin")
print("cos")
print("tan")
print("cot")
print("fact")
print("sqrt")
print("enter your choice: ")
cal = input()
if cal == "+" or cal == "-" or cal == "*" or cal == "/":
    a = float(input("enter first number: "))
    b = float(input("enter secound number: "))
elif cal == "fact":
    a = int(input("please enter integer nember: "))
elif cal == "sqrt":
    a = float(input("please enter posetive nember: "))
else:
    a = float(input("enter the number: "))
   
if cal == "+":
    result= a + b

elif cal == "-":
    result= a - b

elif cal == "*":
    result = a * b

elif cal == "/":
    if b == 0:
        result = print("This number is not exist")
    else:
        result = a / b
elif cal == "sin":
    result = math.sin(a * math.pi / 180)

elif cal == "cos":
    result = math.sin(a * math.pi / 180)

elif cal == "tan":
    result = math.sin(a * math.pi / 180)

elif cal == "cot":
    result = math.sin(a * math.pi / 180)

elif cal == "fact":
    result = math.factorial(a)

elif cal == "sqrt":
    result = math.sqrt(a)
    
print(result)

