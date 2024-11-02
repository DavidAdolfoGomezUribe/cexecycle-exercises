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
        Welcome back Mr/Ms {name}, this is a program for calculate a two multiplication tables from 1 to 10:""") 

    try :    
        
        numberOne = int(input("        First table: "))
        numberTwo = int(input("        Second table: "))
        matrix = []

        for i in range(1,11) : 
            matrix.append(i + (numberOne - 1))

        #Disclaimer: i use this two methods in order to see wich one adapts better for my porpuse, the firs one
        #allows me to do more accurate enhancements  , the second one its a fast way to do a 10x10 table
           
        #First way:
        print (f"\n        ", " ".join(str(num).rjust(3) for num in matrix),
              "\n        ", " ".join(str(2*num).rjust(3) for num in matrix),
              "\n        ", " ".join(str(3*num).rjust(3) for num in matrix),
              "\n        ", " ".join(str(4*num).rjust(3) for num in matrix),
              "\n        ", " ".join(str(5*num).rjust(3) for num in matrix),
              "\n        ", " ".join(str(6*num).rjust(3) for num in matrix),
              "\n        ", " ".join(str(7*num).rjust(3) for num in matrix),
              "\n        ", " ".join(str(8*num).rjust(3) for num in matrix),
              "\n        ", " ".join(str(9*num).rjust(3) for num in matrix),
              "\n        ", " ".join(str(10*num).rjust(3) for num in matrix),"\n"
            )
        
        #Second way:
        for multiplier in range(1, 11):
            print(f"        ", " ".join(str((( numberTwo )  * multiplier ) ).rjust(3) for numberTwo in matrix))


        #so, in both cases i get the correct tables , the only thing is becareful in wich side i put
        #the variables (numberOne and numberTwo)
            
            
            
        
        

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