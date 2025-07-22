#Exceptions and handling
import datetime
try:
    num11= int(input("Ener num11:"))
    num1= int(input("Ener num1:"))
    op=num11/num1
    print("Result :", op)
except Exception as e:
    c= datetime.datetime.now().strftime("%Y - %m - %d %H:%M:%S")
    txt= f"[{ct} Error:{str(e)}]"
    

    


