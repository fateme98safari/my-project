import random
list=[]
n=int(input("enter n: "))
for i in range(n):
    computer_choice=random.randint(0,1000)
    list.append(computer_choice)
print(list)