#Exceptions and handling
try:
    num11= int(input("Ener num11:"))
    num1= int(input("Enter num1:"))
    op=num1/num1
    print("Result :", op)
except ZeroDivisionError:
    print("Can't divide by zero")
    


