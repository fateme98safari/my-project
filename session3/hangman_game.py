import random


words_bank=["red","blue","yellow","pink","purple","gray","black","white","brown","green"]

user_char=[]
good_char=[]
bad_char=[]
sum1=0
sum2=0
counter=0

word=random.choice(words_bank)

for i in range(len(word)):
  sum1= sum1+i
print(sum1)

while counter<6:
    for i in range(len(word)):
      if word[i] in good_char:
        sum2=sum2+i
        print(word[i], end="")

      else:
        print("- ", end="")

    if sum1==sum2:
      print("...you win...")

    else:

       user_char=input("enter your guess: ")  

    if len(user_char)==1:
      if user_char in word:
          good_char.append(user_char)
          print("✔")
      else:
        bad_char.append(user_char)
        counter+=1
        print("⚡")
    else:
        print("enter correct please")