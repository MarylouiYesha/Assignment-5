#Program 2: Addition Quiz
#Create a program that automatically generate two random numbers to add (0 to 99)

import random
print("1. Please add the following numbers")
a=random.randint(0,99)
b=random.randint(0,99)
sum= a + b
print(str(a),"+ " +str(b))

#Let the user answer and evaluate if the user has the correct answer
score=0
ans=int(input("Answer:"))
if ans==sum:
    print("Your answer is correct!")
    score+= 1
else:
    print("Your answer is wrong")

#The program will ask the user 10 addition operation
print("2. Please add the following numbers")
a=random.randint(0,99)
b=random.randint(0,99)
sum= a + b
print(str(a),"+ " +str(b))

ans=int(input("Answer:"))
if ans==sum:
    print("Your answer is correct")
    score+= 1
else:
    print("Your answer is wrong")

print ("Total Score: " + str(score) +"/10")
#Display the result summary of the 10 operations (ex 9/10)
