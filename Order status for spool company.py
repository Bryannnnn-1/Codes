#Problem statement:  to write a program that displays the status of an order. 
#by Bryan
#created on 03nd december 2024
#*************************************************************************************************#


def getInputData():#first function to get the input data
    global numberOfSpoolsOrdered, numberOfSpoolsInStock, shipping#declaring variables
    #getting the numbe of spools ordered
    while True:#loop to get input data
        userInput = input("What is the number of spools ordered: ").strip()
        print(" ")
            #validation checks for the user input
        if not userInput:#make sure the user leaves no blank space
            print("Don't leave the space blank!\nTry again!")#error message
            print("****************************************")
            print(" ")
            continue#gives the user chance to try again
        else:
            try:#try converting the user input to integer
                numberOfSpoolsOrdered = int(userInput)
                if numberOfSpoolsOrdered < 1:#if the user input is less than 1 
                    print("Enter a number from 1!")#error message
                    print("********************************************************")
                    print(" ")
                    continue#gives the user chance to try again
                else:#else
                    break#break if the condition is met
            except ValueError:#if the user input cannot be converted to integer
                print("Enter a digit!\nTry again!")#error message
                print("********************************************************")
                print(" ")
    
    #getting the number of spools in stock
    while True:#loop to get input data
        UserInput = input("How many spools are in stock: ").strip()
        print(" ")

        if not UserInput:#making sure the user leaves no space blank
            print("No blank spaces needed!")#error message
            print("********************************************************")
            print(" ")
            continue#gives the user chance to enter again
        else:
            try:#try converting user input to integer
                numberOfSpoolsInStock = int(UserInput)
                if numberOfSpoolsInStock < 1:#checking if the user input is greater than 0
                    print("Enter a number more than 0!")
                    print("********************************************************")
                    print(" ")
                    continue#gives the user chance to try again
                else:
                    break#break if the conditon is met
            except ValueError:#else the user input cannot be converted to integer
                print("Enter a digit greater than 0\nTry again!")#error message
                print("********************************************************")
                print(" ")
        
    while True:
        print ("Normal shipping is £10 each piece while any special charges is £15 each")
        print("************************************************************************")
        print("1. Normal shipping and handling")
        print("2. Special shipping and handling")                                   #displaying the menu of the shipping
        print(" ")
        print("Choose the type of shipping\nChoose 1 or 2")

        Userinput = input("").strip()#get the user to choose an option

        if not Userinput:#presence check
            print("Do not leave the space blank!")#error message
            print("********************************************************")
            print(" ")
            continue#user to enter again
        else:
            try:#try to convert user input to integer
                shipping = int(Userinput)
                if (shipping < 1) or (shipping > 2):#if the user enters a wrong digit
                    print("Enter 1 or 2!")#error message
                    print("********************************************************")
                    print(" ")
                    continue#gives the user chance to enter again
                elif shipping == 1:#if user input is 1
                    shipping = 10#shiiping is assigned 10
                elif shipping == 2:#if userinput is 2
                    shipping = 15#shipping is assigned 15
                else:#else
                    break#break out of the loop
            except ValueError:#if the user input cannot be converted to integer
                print("Enter either 1 or 2!")#error message
                print("********************************************************")
                print(" ")
            break#break to end the loop

    return numberOfSpoolsInStock, numberOfSpoolsOrdered, shipping#return the variables to be used in another function

    

def computing():#function to calculate the order
    #declare variables
    global backOrder, totalSellingPrice, total, shipping, numberOfSpoolsOrdered, numberOfSpoolsInStock, totalShippingCharge
    
    if numberOfSpoolsOrdered > numberOfSpoolsInStock:#if the number of spools ordered is greter than the number in stock
        backOrder = numberOfSpoolsOrdered - numberOfSpoolsInStock#subtract number in stock from the ordere bnumber
    
    else:#else
        backOrder = 0#the backorder will be 0
    
    print(" ")

    #display the back order
    print(f"The number of spools on back order is '{backOrder}' piece(s)")
    
    print(" ")

    # calculating the total selling price
    totalSellingPrice = numberOfSpoolsOrdered * 100
    
    print(" ")

    #displaying the total selling price
    print(f"The total selling price for '{numberOfSpoolsOrdered}' spools of copper wiring is: £{totalSellingPrice}.00 ")
    
    print(" ")

    #calculating the total shipping price
    totalShippingCharge = shipping * numberOfSpoolsOrdered

    print(" ")

    #displaying the total shipping charge
    print(f"The total shipping and handling fee for '{numberOfSpoolsOrdered}' spools of copper wiring is: £{totalShippingCharge}.00")
    
    print(" ")

    #calculating the total price for the order
    total = totalShippingCharge + totalSellingPrice
    
    print(" ")

    #printing the total price 
    print(f"The total cost for the Order is £{total}.00")
    






def main():#defining a main function to execute the code in order
    print("*************W*E*L*C*O*M*E***T*O***M*Y***P*R*O*G*R*A*M***************")#welcome message
    print(" ")
    getInputData()#calling function
    print("*********************T*H*E***O*R*D*E*R***S*T*A*T*U*S*****************************")
    print(" ")
    #displaying the number of spools ordered
    print(f"The number of spools ordered is '{numberOfSpoolsOrdered}' piece(s) ")
    computing()#calling function
    print(" ")
    print("************T*H*A*N*K*S***F*O*R***U*S*I*N*G***M*Y***P*R*O*G*R*A*M***************")#thanks message




main()#CALLING ON THE MAIN FUNCTION TO RUN THE CODE