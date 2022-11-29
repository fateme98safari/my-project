import math
list1=[]
list2=[]
list3=[]
x1=0
x2=0
LCM=0
num1=int(input("enter the first number: "))
num2=int(input("enter the secound number: "))
for i in range(1,101):
    x1=num1*i
    list1.append(x1)
    x2=num2*i
    list2.append(x2)
for i in range(0,100):
        if list1[i] in list2:
            list3.append(list1[i])
        else:
            continue
LCM = min(list3)
print(LCM)
        

    

