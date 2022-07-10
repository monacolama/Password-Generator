import random as rn
import sys

passwordSaverDict = {}

# A string with all the characters used to write the password
passwordCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~`!@#$%^&*()_-+={[}]|;'<,>.?/"

# The alphabetical key is translated in this function
def keyGenerator():
    key = input("Key: ")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list(alphabet)
    key = key.lower()
    list(key)
    summa = 0
    temp = None

    for char in key:

        # The index of the character is saved in a string variable
        temp = str(alphabet.index(char))

        # If the integer variable is double digit, the digits are added together
        # and added to the sum variable
        if int(temp) >= 10:
            summa += int(temp[0]) + int(temp[1])
        # If not, the number is added to the sum variable
        else:
            summa += int(temp)

    return summa

# The password is crypted in this function
def passwordCryptography(password):
    password = password
    # A new key is generated
    key = keyGenerator()

    # The password becomes a list and a copy of it os created
    passwordList = list(password)
    tempPasswordList = passwordList
    # The string with all the characters becomes a list
    passwordCharactersList = list(passwordCharacters)
    temp = 0

    for char in tempPasswordList:
        for n in passwordCharactersList:
            # The index of the character in the total characters list is saved
            # in a temp variable
            temp2 = passwordCharactersList.index(n)
             # If the character in the password is equal to the 
             # character in the list, it will be crypted
            if char == n:
                # Here is checked the case when the index of the character
                # plus the key is greater than the characters list length.
                # In this case, the list will restart from the index 0
                if (temp2 + int(key)) >= len(passwordCharacters):
                    passwordList[temp] = passwordCharactersList[((temp2 + int(key)) - len(passwordCharactersList))]
                    continue
                # Here the previous case doesn't occur 
                elif (temp2 + int(key)) < len(passwordCharacters):
                    passwordList[temp] = passwordCharactersList[(temp2 + int(key))]
                    continue
                else:
                    print("Error")
                    sys.exit()
        temp += 1

    passwordList = "".join(passwordList)

    return passwordList

# The password and the site are saved in a dictionary in this function
def passwordSaver(password, passwordsite):
    passwordSaverDict[passwordsite] = password

# The password is checked in this function
def passwordChecker(password):
    # Each boolean will have to be true if the password is correct
    checkUpper = False
    checkLower = False
    checkNumber = False
    checkSymbol = False
    finalCheck = False

    # Every character in the password is checked
    # and if there are all the categories of characters
    # the FinalCkeck boolean will be True and returned
    for char in password:

        if char.isupper():
            checkUpper = True
        elif char.islower():
            checkLower = True
        elif char.isnumeric():
            checkNumber = True
        for i in "~`!@#$%^&*()_-+={[}]|;'<,>.?/":
            if char == i:
                checkSymbol = True
            else:
                continue

    if checkUpper and checkLower and checkNumber and checkSymbol:
        finalCheck = True

    return finalCheck


# The password is generated in this function
def passwordGenerator():
    newPassword = ""
    upperCount = 0  # Max 3
    lowerCount = 0  # Max 3
    numberCount = 0  # Max 4
    symbolCount = 0  # Max 4
    loopChecker = True
    # 91 length
    global passwordCharacters

    # For loop to write 14 characters
    for i in range(0, 14):
        loopChecker = True
        # Variable to pick a random number from 0 to 90
        temp = rn.randint(0, 90)

        # In this while loop the password is created 
        while loopChecker:
            # UPPERCASE 
            # If the random character is uppercase and the number of uppercase 
            # letters is lower than 3, the character is added to the password
            # and the uppercase counter increases by 1.
            # If not, the loop will continue to the next condition
            if passwordCharacters[temp].isupper() and upperCount < 3:
                newPassword += passwordCharacters[temp]
                upperCount += 1
                break
            else:
                loopChecker = True

            # If the uppercase counter is equal to 3 and the character
            # is uppercase, a new random integer is generated
            if passwordCharacters[temp].isupper() and upperCount == 3:
                temp = rn.randint(0, 90)

            # LOWERCASE
            # If the random character is lowercase and the number of lowercase 
            # letters is lower than 3, the character is added to the password
            # and the lowercase counter increases by 1.
            # If not, the loop will continue to the next condition
            if passwordCharacters[temp].islower() and lowerCount < 3:
                newPassword += passwordCharacters[temp]
                lowerCount += 1
                break
            else:
                loopChecker = True

            # If the lowercase counter is equal to 3 and the character
            # is lowercase, a new random integer is generated
            if passwordCharacters[temp].islower() and lowerCount == 3:
                temp = rn.randint(0, 90)

            # NUMBERS
            # If the random character is a number and the number of numeric 
            # characters is lower than 4, the character is added to the password
            # and the number counter increases by 1.
            # If not, the loop will continue to the next condition
            if passwordCharacters[temp].isnumeric() and numberCount < 4:
                newPassword += passwordCharacters[temp]
                numberCount += 1
                break
            else:
                loopChecker = True

            # If the number counter is equal to 3 and the character
            # is a number, a new random integer is generated
            if passwordCharacters[temp].isnumeric() and numberCount == 4:
                temp = rn.randint(0, 90)

            # SYMBOLS
            # If the random character is a symbol and the number of symbols 
            # is lower than 3, the character is added to the password
            # and the symbol counter increases by 1.
            # If not, the loop will continue to the next condition
            for j in "~`!@#$%^&*()_-+={[}]|;'<,>.?/":
                if passwordCharacters[temp] == j and symbolCount < 4:
                    newPassword += passwordCharacters[temp]
                    symbolCount += 1
                    loopChecker = False
                    break
                else:
                    loopChecker = True

            # If the symbol counter is equal to 3 and the character
            # is a symbol, a new random integer is generated
            for k in "~`!@#$%^&*()_-+={[}]|;'<,>.?/":
                if passwordCharacters[temp] == k and symbolCount == 4:
                    temp = rn.randint(0, 90)

    return newPassword

def main():
    print("PASSWORD GENERATOR\n")
    # First, the program asks you to write the site for this new password
    passwordSite = input("Write the site: ")

    # The password is generated
    password = passwordGenerator()

    # Check if the password is valid
    while not passwordChecker(password):
        password = passwordGenerator()

    # Print the final password
    print("Final password: " + password + "\n")

    # The password is crypted
    cryptedPassword = passwordCryptography(password)
    
    # The password is saved in a dictionary and then in a text fie
    passwordSaver(cryptedPassword, passwordSite)
    
    passwordTextFile = open("#Text file name", "a")
    for key, value in passwordSaverDict.items():
        passwordTextFile.write('"' + str(key) + '"' + " : \"" + str(value) + "\"\n")
    passwordTextFile.close()


if __name__ == '__main__':
    main()
