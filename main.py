#Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:
#
#12,14,18,116,132,164,…
#en forma decimal:
#
#0.5,0.25,0.125,0.0625,0.03125,0.015625,…
#El programa debe mostrar tres columnas que contengan la siguiente información:
#
#Potencia  Fraccion  Suma
#1         0.5       0.5
#2         0.25      0.75
#3         0.125     0.875
#4         0.0625    0.9375
#...       ...       ...
#El programa debe terminar cuando la fracción decimal sea menor o igual a 0.000001.



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
        Welcome back Mr/Ms {name}, this is a program that allows you to work with the fractional powers of two: \n""") 
        

    try :    
        
        potency = 1 
        fraction = 0.5  
        sum = fraction  

        
        print(f"{'        Potency:':<10} {'  Fraction:':<10}{'  Sum:':<10}")
        print(f"        ______________________________")

        print(f"        {potency:<10} {fraction:<10.6f} {sum:<10.6f}")

        
        while fraction > 0.000001:
            potency += 1  
            fraction = 1 / (2 ** potency)  
            sum = 1 - fraction  
            
            
            print(f"        {potency:<10} {fraction:<10.6f} {sum:<10.6f}")
        
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()

        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")
                break
    except :            
        print("\n        Error: Enter the correct data ")
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()

        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye! \n ")