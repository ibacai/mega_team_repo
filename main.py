
def getDoubleAlphabet(alphabet):
   doubleAlphabet = alphabet + alphabet
   return doubleAlphabet

def getMessage():
   stringToEncrypt = input("Please enter a message to encrypt: ")
   return stringToEncrypt

def getCipherKey():
   shiftAmount = input( "Please enter a key (whole number from 1-25): ")
   return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        # ex. C(2) = A(0) + 2 (cipher key)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

#main code block
#print (getDoubleAlphabet("ABC"))
#print (getCipherKey())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print (encryptMessage(getMessage(), getCipherKey(), getDoubleAlphabet(alphabet)))




#def example():
#  fish = 5
#  return fish
#print(example())
#def printMany(x):
#    for n in range(x):
#      print(f"{n + 1}th time through the loop, print {x}")
    #i = 0
    #while i <= len(range(x)) - 1:
    #  print(f"{i + 1}th time through the loop, print {x}")
    #  i += 1
#print (getDoubleAlphabet("ABC"))
#x = getDoubleAlphabet ("beautiful day")
#print (x)
#print(getMessage())
#printMany(1)
#printMany(2)
#printMany(3)



