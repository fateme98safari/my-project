list1=[]
list2=[]
for i in range(6):
    x=int(input("enter your number: ") )
    list1.append(x)
    
list2=sorted(list1)
print(list2)

if list1==list2:
    print("true")
else:
    print("false")
