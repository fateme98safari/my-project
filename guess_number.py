import random
counter=0
computer_number=random.randint(10,60)
while 1==1:
    user_number = int(input())

    if user_number < computer_number:
        counter=counter+1
        print("go up")
        continue

    elif  user_number > computer_number :
        counter= counter + 1
        print("go down")
        continue

    elif computer_number == user_number:
         counter=counter+1
         print("πππyou winπππ")
         print("number of your geusses: " , counter)
         break

