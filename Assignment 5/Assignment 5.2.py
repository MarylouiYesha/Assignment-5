#Program 2: Find the lowest number
#Create a program that ask 3 numbers. 
#Find the lowest number using only if-else statement.
#Display the lowest number
a=(float(input("Please enter your first number:")))
b=(float(input("Please enter your second number:")))
c=(float(input("Please enter your third number:")))

def lowest(): 
    if a and b> c:
       return c
    elif b and c> a:
        return a
    elif c and a > b:
        return b
final = lowest()
print (final)
