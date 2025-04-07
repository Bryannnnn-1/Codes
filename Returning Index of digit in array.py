#Problem statement:  to write a program that will search for a specific value in a array and output its index
#by Bryan
#created on 02nd december 2024
#*************************************************************************************************#

import array as arr#importing the array

ListOfNumbers= arr.array('i',[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])#listing the array containing only integers



def getInputToSearchFor():#creating function to get input data
    global number#declaring variable
    while True:#loop to get input data
        print("Which number do you want to search for?")
        userInput = input("")#get input data

        if not userInput:#presence check
            print("Don,t leave the space blank!")
            print("*****************************************************************")
            print(" ")
            continue#give the user chance to enter again
        else:


            try:#try converting the input to integer
                number = int(userInput)
                break
            except ValueError:#if it cannot be converted to integer
                print("This is not a valid input!")
                print("************************************************************")
                print(" ")

def searchForTheInputInTheArray():#function to search for the value in the array
    global number#declaring variables

    if number in ListOfNumbers:#checking if the number is in the array
        print(f"...And, the Value '{number}' is found at index {ListOfNumbers.index(number)} of the Array!")
    else:#if not, print value not found
        print(f"...Opss! the Value '{number}' not Found!")

def main():#defining a main function to run the code
    print("*************W*E*L*C*O*M*E***T*O***M*Y***P*R*O*G*R*A*M*!***************")
    print(ListOfNumbers)
    print(" ")
    getInputToSearchFor()#calling function
    print(f"The number you inputted is '{number}' ")
    print(" ")
    searchForTheInputInTheArray()#calling function
    print(" ")
    print("************E*N*D***O*F***M*Y***P*R*O*G*R*A*M*!*****************")


main()##calling the main fuction for the code to be executed