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
        Welcome back Mr/Ms {name}, this is a program for calculate the aprox value of π using Leibniz series: \n""") 
        

    try :    
        n = int(input(f"""        Select the number of iterations: """))

        if n <= 0 :
            print(f"\n        Positive numbers only") 
        else:
            if n > 0 and n < 10000000:
                
                sLeibniz = 0
                for i in range(n):
                    sLeibniz += ((-1) ** i) / (2 * i + 1)
                
                pi = 4 * sLeibniz
                print(f"\n        {round(pi,11)}")

            
            elif n >= 10000000:
                    
                continueAsk = input( "\n        Maybe your PC can slow down after this number of iterations. Do you want to continue? (yes/no): " ).strip().lower()

                if continueAsk == "yes" :
                    sLeibniz = 0
                    for i in range(n):
                        sLeibniz += ((-1) ** i) / (2 * i + 1)
                    
                    pi = 4 * sLeibniz
                    print(f"\n        {round(pi,11)}")
                
            

            else:
                print(f"        use a lower number of iterations")   
        
    
  
    
       
              
        
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()

        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break
    except :            
        print("\n        Error: Enter the correct data ")
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()

        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")