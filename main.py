#Escriba un programa que entregue todos los divisores del número entero ingresado:
#
#Ingrese numero: 200
#1 2 4 5 8 10 20 25 40 50 100 200

import math
import sys
import time



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
        Welcome back Mr/Ms {name}, this is a program for print 3 types of three types of figures : \n""") 
        

    try :    
        select = int(input(f"""        Select the figure that you want :
        1) for square
        2) for triangle
        3) for hexagon \n
        """))
        print("")
        if select > 0 and select < 4:
           
            spin_chars = ['|', '/', '-', '\\'," "]
            for i in range(2):
                                
                for char in spin_chars:
                    
                    sys.stdout.write(f'\r        {char}')
                    sys.stdout.flush()
                    time.sleep(0.1)
                    
            if select == 1:    
                
                width = int(input("\n        Select the width: "))
                heigth = int(input("        Select the heigth:  "))
                
                if width >= 1 and heigth >= 1 :    
                    
                    print("")
                    matrix = ["*"] * width

                    for i in range(heigth):
                        print("        "," ".join(matrix))
                
                else:
                    print("\n        Positive numbers only")

            if select == 2:
                
                heigth = int(input("\n        Select the heigth:  "))
                
                if  heigth >= 1 :            
                    matrix = [] 
                    print("")
                    for i in range(2 , (heigth + 2 )):
                        matrix.append("*")
                        print("        "," ".join(matrix))
                else:
                    print("\n        Positive numbers only")

            if select == 3:
                
               
                size = int(input("\n        Select the size: "))
                print("")
                
                if size >= 1  :            
                    for i in range(size):
                        
                        blanck = ' ' * (size - i - 1)
                        
                        dots = '*' * (size + 2 * i)
                        
                        print("        ",blanck + dots)
                    
                    for i in range(size -2,-1,-1):
                    
                        blanck = ' ' * (size - i - 1)
                    
                        dots = '*' * (size + 2 * i)
                    
                        print("        ",blanck + dots)
                else:
                    print("\n        Positive numbers only")


        else:
            print ("\n        select the correct program")


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