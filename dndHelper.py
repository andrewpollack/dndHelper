
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
    cont = "yes"
    while(cont.lower() == "yes"): 
        
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


def loadClassDictionary():
    class_dict = dict()
    with open("utils/classes.txt", 'r') as ctxt_file:
        curr_class = list()
        curr_name = ""
        for cline in ctxt_file:
            # End of Current Class
            if(cline.rstrip() == "***"):
                class_dict[curr_name] = curr_class
                curr_class = list()
            elif(cline.split(":")[0] == "Name"):
                curr_name = " ".join(cline.split(":")[1:]).rstrip().lstrip().lower()
                curr_class.append(cline.rstrip())
            else:
                curr_class.append(cline.rstrip())
    return class_dict


def classInformationMenu():
    """
    Basic class information section of the helper.
    """
    print("\n~*~ Welcome to the class information section! ~*~") 
    print("(Note: Thank you to the website 'dndbeyond' for their short class descriptions.)")
    class_dict = loadClassDictionary()
    classes = list(class_dict.keys())
    classes.sort()
    # Undercase classes used for input checks
    uclasses = [x.lower() for x in classes]
    classes = [x.title() for x in classes]
    cont = "yes"
    while(cont.lower() == "yes"): 
        u_class = input("\nWhat class would you like to learn about?\nAll\n" + "\n".join(classes) + "\n\nClass: ").lower()
        while u_class not in uclasses and u_class != "all":
            print("\nPlease enter a valid class.")
            u_class = input("What class would you like to learn about?\n\nClass: ").lower()
        # Print full information of all classes.
        if(u_class == "all"):
            print("Here's a basic list of the classes and their information!")
            for curr_class in uclasses:
                print("\n" + class_dict[curr_class][0])
                for curr_info in class_dict[curr_class][1:]:
                    print(" " + curr_info)
        # Print full information of specified class.
        else:
            print("\n" + class_dict[u_class][0])
            for curr_info in class_dict[u_class][1:]:
                print(" " + curr_info)
        cont = input("\nWould you like to learn about another class?  Yes/No: ")
    print("\nReturning to main menu...\n\n\n")


def mainMenu():
    u_input = "default_text"
    while(True):
        u_input = str(input("What do you need?\n1 DiceRoll\n2 Beastiary\n3 ClassInformation\n4 Exit\n\nInput: "))
        if(u_input == "1" or u_input.lower() == "diceroll" or u_input.lower() == "dice roll"):
            print("Entering Dice Rolling Menu...")
            diceRollMenu()
        elif(u_input == "2" or u_input.lower() == "beastiary"):
            print("\nEntering Beastiary Menu...")
            print("((Work in progress, returning to menu))")
        elif(u_input == "3" or u_input.lower() == "classinformation" or u_input.lower() == "class information"):
            print("\nEntering Class Information Menu...")
            classInformationMenu()
        elif(u_input == "4" or u_input.lower() == "exit" or u_input.lower() == "e"):
            return
        else:
            print("I don't quite recognize your input, please try again!")


def main(): 
    print("~*~ Welcome to dndHelper! ~*~\n\n")
    mainMenu()
    print("Thank you for playing!  Exiting now.") 

main()
