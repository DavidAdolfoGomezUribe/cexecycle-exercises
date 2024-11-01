#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos.
#Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.
#
#Ingrese num: 1
#Ingrese num: 7
#La suma es 20
#
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
        Welcome back Mr/Ms {name}, this is a program for calculate the potentiation of the number 2.
              """) 

    try :    
        aDigit = int(input("        Enter the amount: "))
        
        if aDigit >= 1:

            for i in range(0,aDigit) :
                total = math.pow(2, i )
                
                print(f"        {round(total)}")
        else:        
            print ("\n        Positive numbers only")

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