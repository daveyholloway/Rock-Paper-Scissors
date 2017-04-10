# Rock, Paper, Scissors
# 'nuff said!
#
# Modification History
# ====================
#
# When       Who             Why
# ========== =============== ===========================================
# 14/02/2016 Dave            Initial Version
#
import random

# A function to get user input and return 1,10 or 100
def getUserChoice():
    # Ask for some user input
    choice=input("Enter R, P or S : ")
    # If it's not a valid response then ask again!
    while (choice.upper() not in ("R","P","S")):
        choice=input("No, really - enter R, P or S : ")

    # Must be valid if we're here so return a value based on
    # the choice
    if choice.upper() == "R":
           return(1)
    elif choice.upper() == "P":
           return(10)
    else:
           return(100)

# A function to print Rock, Paper, Scissors depending on the value passed in
def displayWeapon(weaponNumber):
    if weaponNumber == 1:
        return("Rock")
    elif weaponNumber == 10:
        return("Paper")
    elif weaponNumber == 100:
        return("Scissors")
    else:
        return("Arg! - Call the support team!!")

# Step 0 - A bit of setting up
userMultiplier = 1
compMultiplier = 2

userScore = 0
compScore = 0

tries = 5

while tries>0:

    # Step 1 - Computer makes a choice
    compChoice = (10**random.randint(0,2)) * compMultiplier
    # The computer choice will be:
    # 
    # 2   : Rock
    # 20  : Paper
    # 200 : Scissors
    # 

    # Step 2 - User is asked for their choice
    userChoice = getUserChoice() * userMultiplier
    # The user choice will be:
    # 
    # 1   : Rock
    # 10  : Paper
    # 100 : Scissors
    #

    # Step 2.5 - Display the choices
    print("You chose " + displayWeapon(userChoice/userMultiplier))
    print("I chose " + displayWeapon(compChoice/compMultiplier))

    # Step 3 - Determine who won and let us know
    # Adding the user and computer choice together should tell us who won!
    #
    # Draw      : 3, 30, 300
    # Comp Wins : 102, 21, 210
    # User Wins : 201, 12, 120
    score = userChoice + compChoice

    # Was it a draw?

    if score in (3,30,300):
        print("It's a draw!")
    elif score in (102,21,210):
        print("Computer wins! - In your face!!")
        compScore = compScore + 1
    elif score in (201,12,120):
        print("User wins! - Go you!")
        userScore = userScore + 1
    else:
        print("There's something very wrong!!")

    # Step 4 - Repeat
    # decrement the try count
    tries = tries - 1

print ("Done !")
print ("You scored " + str(userScore))
print ("I scored " + str(compScore))
if userScore>compScore:
    print("You Won!")
elif userScore<compScore:
    print("I won! - puny human!!")
else:
    print("A draw! - I wasn't expecting that!")
