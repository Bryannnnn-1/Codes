#Problem statement: to count how many even and odd numbers are in a given array of integers.
#By Bryan 

import array as arr

numArray = []#Creating an empty array

def getInputData():#defining a function to get input data
    global length, numArray
    while True:
        userInput = input("How many number do you want to check: ")#getting the length of number
        
        try:
            length = int(userInput)
            break
        except ValueError:
            print("This is not a valid number...Please try again!")
            print("**********************************************")
            return getInputData()
        
def Body(): 
    global Odd, even       
    x = 1 #initialise
    Odd = 0
    even = 0     
    
    while x <= length:#A loop to get the digits
        while True:
            userInput = input("Enter Digit - ")#getting the length of number
        
            try:
                digits = int(userInput)
                break
            except ValueError:
                print("This is not a valid number...Please try again!")
                print("**********************************************")
       
        numArray.append(digits)#assigning the digits to the empty array


               

        if digits % 2 == 0:
            even += 1
        else:
            Odd += 1
        
        x += 1
        
    return Odd, even


getInputData()
Odd, even = Body()#calling the function

print()
print(numArray)
print()
print("Even numbers in the Array: ", even)
print("Odd numbers in the Array: ", Odd)


