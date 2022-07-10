import random as rn
import sys

passwordSaverDict = {}
passwordCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~`!@#$%^&*()_-+={[}]|;'<,>.?/"

def keyGenerator():
    key = input("Key: ")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list(alphabet)
    key = key.lower()
    list(key)
    summa = 0
    temp = None

    for char in key:

        temp = str(alphabet.index(char))

        if int(temp) >= 10:
            summa += int(temp[0]) + int(temp[1])
        else:
            summa += int(temp)

    return summa

def passwordCryptography(password):
    password = password
    key = keyGenerator()

    passwordList = list(password)
    tempPasswordList = passwordList
    passwordCharactersList = list(passwordCharacters)
    temp = 0

    for char in tempPasswordList:
        for n in passwordCharactersList:
            temp2 = passwordCharactersList.index(n)
            if char == n:
                if (temp2 + int(key)) >= len(passwordCharacters):
                    passwordList[temp] = passwordCharactersList[((temp2 + int(key)) - len(passwordCharactersList))]
                    continue
                elif (temp2 + int(key)) < len(passwordCharacters):
                    passwordList[temp] = passwordCharactersList[(temp2 + int(key))]
                    continue
                else:
                    print("Error")
                    sys.exit()
        temp += 1

    passwordList = "".join(passwordList)

    return passwordList

def passwordSaver(password, passwordsite):
    passwordSaverDict[passwordsite] = password

def passwordChecker(password):
    checkUpper = False
    checkLower = False
    checkNumber = False
    checkSymbol = False
    finalCheck = False

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


def passwordGenerator():
    newPassword = ""
    upperCount = 0  # Max 3
    lowerCount = 0  # Max 3
    numberCount = 0  # Max 4
    symbolCount = 0  # Max 4
    loopChecker = True
    # 91 len
    global passwordCharacters

    for i in range(0, 14):
        loopChecker = True
        temp = rn.randint(0, 90)

        while loopChecker:
            if passwordCharacters[temp].isupper() and upperCount < 3:
                newPassword += passwordCharacters[temp]
                upperCount += 1
                break
            else:
                loopChecker = True

            if passwordCharacters[temp].isupper() and upperCount == 3:
                temp = rn.randint(0, 90)

            if passwordCharacters[temp].islower() and lowerCount < 3:
                newPassword += passwordCharacters[temp]
                lowerCount += 1
                break
            else:
                loopChecker = True

            if passwordCharacters[temp].islower() and lowerCount == 3:
                temp = rn.randint(0, 90)

            if passwordCharacters[temp].isnumeric() and numberCount < 4:
                newPassword += passwordCharacters[temp]
                numberCount += 1
                break
            else:
                loopChecker = True

            if passwordCharacters[temp].isnumeric() and numberCount == 4:
                temp = rn.randint(0, 90)

            for j in "~`!@#$%^&*()_-+={[}]|;'<,>.?/":
                if passwordCharacters[temp] == j and symbolCount < 4:
                    newPassword += passwordCharacters[temp]
                    symbolCount += 1
                    loopChecker = False
                    break
                else:
                    loopChecker = True

            for k in "~`!@#$%^&*()_-+={[}]|;'<,>.?/":
                if passwordCharacters[temp] == k and symbolCount == 4:
                    temp = rn.randint(0, 90)

    return newPassword

def main():
    print("PASSWORD GENERATOR\n")
    passwordSite = input("Write the site: ")

    # Generate a new password
    password = passwordGenerator()

    # Check if the password is valid
    while not passwordChecker(password):
        password = passwordGenerator()

    print("Final password: " + password + "\n")

    cryptedPassword = passwordCryptography(password)
    print(cryptedPassword + "\n")
    # Save the password in a dictionary and then in a text fie
    passwordSaver(cryptedPassword, passwordSite)
    passwordTextFile = open("allPass.txt", "a")
    for key, value in passwordSaverDict.items():
        passwordTextFile.write('"' + str(key) + '"' + " : \"" + str(value) + "\"\n")
    passwordTextFile.close()


if __name__ == '__main__':
    main()
