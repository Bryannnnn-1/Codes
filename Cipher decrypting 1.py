import time

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

EncryptAlpha = ["G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F"]

encryptedMessage = ""

def getUserInput():
    global message

    bryan = True

    while bryan:

        print("Enter an Encrypted Message to be Decrypted")

        message = input(">>>>> ").upper().strip()


        if message == "":
            print("Do not leave any blank space!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            bryan = True
        elif not (words.isalpha() or not words.isspace() for words in message):
            print("The encrypted message cannot contain numbers!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" ")
            bryan = True
        else:
            return message
        


def decryption():
    global message, encryptedMessage

    for words in message:
        if words in alphabet:
            IndexOfLetter = alphabet.index(words)

            encryptedMessage += EncryptAlpha[IndexOfLetter]

        else:
            encryptedMessage += words



def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~Welcome to my decryptor by Bryan~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~This program can encrypt on letters and numbers!~~~~~~~~~~~~~~~")
    print(" ")
    print("The numbers will remain the same!")
    print(" ")
    getUserInput()
    decryption()
    print("The Decrypted message is: ")
    print(f"{message}")
    print(" ")
    print("The Encrypted message is: ")
    print(" ")
    time.sleep(1)
    print("Hold on...")
    print(" ")
    time.sleep(1)
    print("Cracking code...")
    print(" ")
    time.sleep(1)
    print(f" '{encryptedMessage}' ")


main()