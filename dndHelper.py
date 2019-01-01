
import random
import time

def rollDice(digit, num_dice):
    """
    Simulates rolling {num_dice} number of {digit} dice.
    """ 
    rolls = list()
    for i in range(num_dice):
        rolled = random.randint(1, digit)
        print("**rolls a " + str(rolled) + "**")
        rolls.append(rolled)
    return sum(rolls)


def diceRollMenu():
    """
    Dice rolling section of the helper.
    """
    print("\n~*~ Welcome to the dice rolling section! ~*~")
    cont = "y"
    while(cont[0].lower() == "y"): 
        
        # Finding digit of dice
        u_digit = input("\nWhat digit dice would you to roll?\nD-")
        while not u_digit.isdigit():
            print("\nPlease enter a valid integer value for your digit.")
            u_digit = input("What digit dice would you to roll?\nD-")
        
        # Finding number of dice to roll
        u_num_dice = input("\nHow many dice would you like to roll?\nNumber of dice: ")
        while not u_num_dice.isdigit():
            print("\nPlease enter a valid integer value for your number of dice.")
            u_num_dice = input("How many dice would you like to roll?\nNumber of dice: ")
        
        roll_tot = rollDice(int(u_digit), int(u_num_dice))
        print("\nIn total, you rolled: " + str(roll_tot) + "!") 
        # Flavor text
        # time.sleep(1)
        cont = input("\nWould you like to roll another set of dice?  Yes/No: ")
    print("\nReturning to main menu...\n\n\n")


def mainMenu():
    u_input = "default_text"
    while(True):
        u_input = str(input("What do you need?\n1 DiceRoll\n2 CharacterCreation\n3 Exit\n\nInput: "))
        if(u_input == "1" or u_input.lower() == "diceroll" or u_input.lower() == "dice roll"):
            print("Entering Dice Rolling Menu...")
            diceRollMenu()
        elif(u_input == "2" or u_input.lower() == "charactercreation" or u_input.lower() == "character creation"):
            print("\nEntering Character Creation Menu...")
            print("((Work in progress, returning to menu))")
        elif(u_input == "3" or u_input.lower() == "exit" or u_input.lower() == "e"):
            return
        else:
            print("I don't quite recognize your input, please try again!")


def main(): 
    print("~*~ Welcome to dndHelper! ~*~\n\n")
    mainMenu()
    print("Thank you for playing!  Exiting now.") 

main()
