#Problem statement:  to write a program that will help its staff calculate the cost of supercar experiences for their customers.
#Created on 11th December 2024
#By Bryan
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#




CustomerDetails = []#creating an empty list

totalCost = 0#initialising total cost

def getInputData():#getting input data of the customer
    global CustomerDetails
    while True:#loop to get the customer name
        name = input("Enter the Customer's Name: ").strip()
       
        if not name:#presence check
            print("Don't leave the space blank!")
            print("*****************************")
            continue
        elif not name.isalpha():#type check
            print("Invalid Input\nTry Again!")
            print("*****************************")
            continue
        else:
            CustomerDetails.append(name)#adding to the list
            break
            

    while True:#loop to get the customer address
        address = input("Enter the Customer's Address: ")

        if not address:#presense check
            print("Don't leave the space blank!")
            print("****************************")
            continue
        else:
            CustomerDetails.append(address)#adding to the list
            break


    while True:#loop to get the customer phone number
        userInput = input("Enter the Customer's Phone Number(eg. 07123456789): ")

        if not userInput:#presence check
            print("Don't leave the space blank!")
            print("*****************************")
            continue
        elif len (userInput) != 11:#length check
            print("Invalid Phone Number!\nTry again")
            print("*****************************")
            continue

        try:#try to convert the userinput to integer
            PhoneNumber = int(userInput)
            CustomerDetails.append(PhoneNumber)#adding the number to the list
            break
        except ValueError:
            print("Invalid Input\nTry Again!")
            print("************************")


def getNumberOfCars():#getting number of cars
    global NumberOfCarsDriven
    while True:#loop to get the number of cars driven
        NumberOfCarsDriven = input("How Many Cars did the Customer Drive: ")

        if not NumberOfCarsDriven:#presence check
             print("You can't leave the space blank!")
             print("***************************")
             continue

        try:#try to convert the userinput to integer
            NumberOfCarsDriven = int(NumberOfCarsDriven)

            if NumberOfCarsDriven < 0 or  NumberOfCarsDriven > 5:#range check
                print("The Customer can minimum drive 1 car and maximum of 5 cars! ")
                continue
            else:
                CustomerDetails.append(f"{NumberOfCarsDriven} car(s)")#adding to the list
                break
        except ValueError:
            print("Invalid Input\nTry Again!")
            print("************************")

        

def getCarType():#getting the car type
    global NumberOfCarsDriven, totalCost#declaring global variables
    
    
    x = 1    
    while x <= NumberOfCarsDriven:#loop to get number of cars driven
        print("**********************************************************")
        print("1. Lamborghini Gallardo - £59 ")
        print("2. Lamborghini Huracan - £59 ")
        print("3. Ferrari F40 - £49 ")
        print("4. Porsche Boxster - £39 ")                                   ###list of cars
        print("5. Audi A5 - £39 ")
        print("6. BMW i8 - £39 ")
        print("7. Lotus Elise - £30 ")
        print("*********************************************************")
        print(" ")

        
        CarType = input( "Enter the type of car driven\nChoose from 1 to 7: ")

        if not CarType:#presense check
            print("Choose car(s) please!")
            print("************************")
            continue
            
                
        try:
            CarType = int(CarType)#type check
            if CarType <= 0 or CarType >= 8:#range check
                print("Invalid choice!\n Select a number from 1 to 7!")
                continue
            else:
                if CarType == 1:
                    totalCost += 59
                elif CarType == 2:
                    totalCost += 59
                elif CarType == 3:
                    totalCost += 49
                elif CarType == 4:
                    totalCost += 39           ####calulating total cost of the test with the cars
                elif CarType == 5:
                    totalCost += 39
                elif CarType == 6:
                    totalCost += 39
                else:
                    totalCost += 30
                x += 1#increment
        except ValueError:
            print("Please Enter a Number from 1 to 7!")
                
        

def getNumberOfLaps():#getting nnmber of laps
    global totalCost, extralaps#declaring global variables
    extralapsCost = 15
    while True:#loop to get extra laps if any
        extralaps = input("How many extra laps: ").strip()

        if not extralaps:#presense check
            print("You can't leave the space blank!")
            print("**********************************")
            continue

        try:
            extralaps = int(extralaps)
            if extralaps >= 1:#calculating extra laps
                totalCost = totalCost + (extralaps * extralapsCost)
                print(f"Each extra lap cost: £{extralapsCost} ")
                print(f"Extra Lap: {extralaps} lap(s) for £{extralaps * extralapsCost}")
                print("***************************************************************")
                break
            else:
                break
        except ValueError:
            print("Enter a valid Number")
            print("**************************************")




def main():
    getInputData()#calling function
    getNumberOfCars()#calling function
    getCarType()#calling function
    getNumberOfLaps()#calling function
    print("****************************************************")
    print(CustomerDetails)
    print(f"The Customer name: {CustomerDetails[0]} ")
    print(f"The Customer address: {CustomerDetails[1]} ")
    print(f"The Customer Phone number: {CustomerDetails[2]} ")              ###learned formatting string today:)
    print(f"The Customer drove: {CustomerDetails[3]} ")
    print("The Customer extra lap(s): ",extralaps)
    print(f"Total Cost is: £{totalCost}.00 ")


main()#calling main function to run the code

