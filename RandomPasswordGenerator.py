import random#importing the random module
import string#importing the string module



def getInputData():#function to get input data
    global userName, email
    while True:
        userName = input("Enter your Username: ")#getting the username
        print(" ")

        if userName == "":#presence check
            print("Enter a name please!")#error message
            print("*************************************")
            continue#give the user chance to enter again
        else:
            break#break out of the loop if the input meets the condition needed


    while True:#while loop
        
        email = input("Please enter your e-mail: ").strip()#getting the email
        print(" ")


        if email == "":#presence check
            print("No blank space please")#error message
            print("**************************************************")
            continue#gives the user chance to enter again
        elif '@gmail.com' not in email:#email validation
            print("Try again please; Enter in this format 'gmail@gmail.com' ")#error message
            print("****************************************************************")
            continue#gives the user chance to enter again
        else:
            break#break out of the loop if the condition is met



def RandomPasswordGenerator():#function to generate a random password 

    LENGTH = 15#constant to initialise the lenght of the password

    passwordCharacter = string.ascii_letters + string.digits + string.punctuation#the password characters

    password = ''.join(random.choices(passwordCharacter, k = LENGTH))#generating the random password

    print(f"This is your random password: {password}")#printing the random password


def main():
    getInputData()#calling the function
    print(" ")
    print(f"The username is: {userName}")
    print(" ")
    print(f"The email is: {email}")
    print(" ")
    RandomPasswordGenerator()#calling function


main()