#Program 3: Life stages
#Create a program that ask for an age of a person
#Display the life stage of the person.
#Rules:
#0 - 12 : Kid
#13 - 17 : Teen
#18 : Debut
#19 above : Adult
your_age= int(input("Please enter your age:"))
if your_age >=0 and your_age <=12:
    print ("Kid")
elif your_age >= 13 and your_age <= 17:
    print ("Teen")
elif your_age == 18:
    print ("Debut")
elif your_age == 19 or your_age>19:
    print ("Adult")
