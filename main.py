#Escriba un programa que entregue todos los divisores del número entero ingresado:
#
#Ingrese numero: 200
#1 2 4 5 8 10 20 25 40 50 100 200

import math



print(f""" 
    ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
     ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝                                                        
                                """) 
name = input("    Hello, please enter your full name:  ")

while True:

    print(f""" \n
        Welcome back Mr/Ms {name}, this is a program for calculate the time in format Hours:Minuts based on the minuts that you put in for your travel: \n""") 


    try :    
        tTime = 0
        while True:
            time = 0
            time = int(input("        Enter the minutes: "))
            
            if time == 0:
                break
            elif time > 0:
                tTime += time
                
                
            else:
                print("\n        Enter a valid time\n")
        
        tHours = tTime // 60
        tMinuts = tTime % 60

        print(f"\n        The time {time} in format HH:MM is {tHours}:{tMinuts} hours for your travel")
        
       #  if not (aSide + bSide > cSide and aSide + cSide > bSide and bSide + cSide > aSide):
       #     raise ValueError("") #posiblemente lo use mas tarde
       
         
        
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()

        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break
    except :            
        print("\n        Error: Enter the correct data ")
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()

        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")