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
        Welcome back Mr/Ms {name}, this is a program for calculate the sum of the number of numbers between  the first and the second number:""") 

    try :    
        digitOne = int(input("\n        Enter the first number: "))
        digitTwo = int(input("        Enter the second number: "))
        total = []
        

        if digitOne  >= 0 and digitTwo >= 0 :

            for i in range( (digitOne + 1),digitTwo) :
               
                total.append(i)

            rTotal = str(sum(total))
            print(f"\n        The sum of the number of numbers between {digitOne} and {digitTwo} is equal to" , " + ".join(map(str,total)) , "=",rTotal )
            
            
            
        
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