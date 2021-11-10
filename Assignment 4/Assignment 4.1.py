import math

def quan():
    apple= int(input("Enter apple quantity:"))
    orange= int(input("Enter orange quantity:"))
    return apple, orange

apple, orange =quan()

def price_fruits():
    applep=20
    orangep=25
    return applep,orangep

applep,orangep= price_fruits()

def total_aprices(apple,applep):
    return apple*applep

def total_oprices(orange,orangep):
    return orange*orangep

o_totala=total_aprices(apple,applep)
o_totalo=total_oprices(orange,orangep)

def grand_total(o_totala,o_totalo):
    return o_totala+o_totalo

    
print(f"The total amount is {grand_total(o_totalo,o_totala)} pesos.")

