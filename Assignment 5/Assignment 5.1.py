import math
agrade=(input("Enter your grade:\n")) 
if agrade == "Inc.":
        print("Grade/Mark: Inc.")
        print("Description: Incomplete")
elif agrade == "W":
        print("Grade/Mark: W")
        print("Description: Withdrawn")
elif agrade == "D":
        print("Grade/Mark: D")
        print("Description: Dropped")

your_grade=(float(input("Enter your grade:")))

if your_grade>= 97 and your_grade<= 100:
          print("Grade/Mark:1.0")
          print("Description: Exellent")
elif your_grade >=94 and your_grade<= 96.4:
         print("Grade/Mark:1.25")
         print("Description: Exellent")
elif your_grade >=91 and your_grade<=93.4:
         print("Grade/Mark:1.5")
         print("Description: Very Good")
elif your_grade >=88 and your_grade<=90.4:
         print("Grade/Mark:1.75")
         print("Description: Very Good")
elif your_grade >=85 and your_grade<=87.4:
         print("Grade/Mark:2.0")
         print("Description: Good")
elif your_grade >=82 and your_grade<=84.4:
         print("Grade/Mark:2.25")
         print("Description: Good")
elif your_grade >=79 and your_grade<=81.4:
         print("Grade/Mark:2.5")
         print("Description: Good")
elif your_grade >=76 and your_grade<=78.4:
         print("Grade/Mark:2.75")
         print("Description: Satisfactory")
elif your_grade ==75:
         print("Grade/Mark:3.0")
         print("Description: Passing")
elif your_grade >=65 and your_grade<=74.4:
         print("Grade/Mark:5.0")
         print("Description: Failure")


