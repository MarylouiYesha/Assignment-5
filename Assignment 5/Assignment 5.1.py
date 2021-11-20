import math
your_grade=(input("Enter your grade:\n")) 

if your_grade == "Inc.":
        print("Grade/Mark: Inc.")
        print("Description: Incomplete")
elif your_grade == "W":
        print("Grade/Mark: W")
        print("Description: Withdrawn")
elif your_grade == "D":
        print("Grade/Mark: D")
        print("Description: Dropped")
else:
        your_grade=float(your_grade)
        if int(your_grade+0.5)>= 97 and int(your_grade+0.5)<= 100:
         print("Grade/Mark:1.0")
         print("Description: Exellent")
        elif int(your_grade+0.5) >=94 and int(your_grade+0.5)<= 96:        
         print("Grade/Mark:1.25")
         print("Description: Exellent")
        elif int(your_grade+0.5) >=91 and int(your_grade+0.5)<=93:
         print("Grade/Mark:1.5")
         print("Description: Very Good")
        elif int(your_grade+0.5) >=88 and int(your_grade+0.5)<=90:
         print("Grade/Mark:1.75")
         print("Description: Very Good")
        elif int(your_grade+0.5) >=85 and int(your_grade+0.5)<=87:
         print("Grade/Mark:2.0")
         print("Description: Good")
        elif int(your_grade+0.5) >=82 and int(your_grade+0.5)<=84:
         print("Grade/Mark:2.25")
         print("Description: Good")
        elif int(your_grade+0.5) >=79 and int(your_grade+0.5)<=81:
         print("Grade/Mark:2.5")
         print("Description: Good")
        elif int(your_grade+0.5) >=76 and int(your_grade+0.5)<=78:
         print("Grade/Mark:2.75")
         print("Description: Satisfactory")
        elif your_grade ==75:
         print("Grade/Mark:3.0")
         print("Description: Passing")
        elif int(your_grade+0.5) >=65 and int(your_grade+0.5)<=74:
         print("Grade/Mark:5.0")
         print("Description: Failure")
        


