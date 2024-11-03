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
        Welcome back Mr/Ms {name}, this is a program for calculate all the divisors of the entered integer """) 


    try :    
        
        numberOne = int(input("        Insert the number: "))
        
        matrix = []

        if numberOne == 0 :
            print("\n        Division by zero cant be possible")


        if numberOne > 0 :   
            for i in range(1, numberOne + 1):
                if numberOne % i == 0:
                    matrix.append(i)

            print (f"\n        The numbers that are divisors of {numberOne} are : ", " ".join(str(num).rjust(1) for num in matrix))
        
        if numberOne < 0 :   
            for i in range( 1,((abs(numberOne)) + 1)  ):
                if numberOne % -i == 0:
                    matrix.append(i)

            print (f"\n        The numbers that are divisors of {numberOne} are : ", " ".join(str(num).rjust(1) for num in matrix))
        
   
        
        
            
            
            
        
        

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