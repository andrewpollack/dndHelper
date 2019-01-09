
import random
import time


def smartGuess(u_input, option_list):
    """
    Naive approach to guessing what the user has input in case
    they didn't enter an exact choice.  Done so by taking highest percentage
    of matching characters between the user's input and an option within the 
    list.
    """
    if u_input in option_list:
        return u_input
    best_match_percent = -100
    best_match_item = ""
    for curr_item in option_list:
        curr_len = len(curr_item)
        copy_item = curr_item
        for curr_letter in u_input:
            let_pos = copy_item.find(curr_letter)
            if(let_pos != -1):
                copy_item = copy_item[:let_pos] + copy_item[let_pos+1:]
        curr_match_percent = (curr_len - len(copy_item)) / curr_len - (len(u_input) / curr_len)
        if(curr_match_percent > best_match_percent):
            best_match_percent = curr_match_percent
            best_match_item = curr_item
    return best_match_item


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
        cont = smartGuess(input("\nWould you like to roll another set of dice?  Yes/No: "), ["yes", "no"])
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
    uclasses = classes
    classes = [x.title() for x in classes]
    cont = "yes"
    while(cont.lower() == "yes"):
        u_class = smartGuess(input("\nWhat class would you like to learn about?\nAll\n" + "\n".join(classes) + "\n\nClass: ").lower(), uclasses)
        # Print all information on classes.
        if(u_class == "all"):
            print("Here's a basic list of the classes and their information!")
            for curr_class in uclasses:
                if(curr_class == "all"):
                    pass
                else:
                    print("\n" + class_dict[curr_class][0])
                    for curr_info in class_dict[curr_class][1:]:
                        print(" " + curr_info)
        # Print full information of specified class.
        else:
            print("\n" + class_dict[u_class][0])
            for curr_info in class_dict[u_class][1:]:
                print(" " + curr_info)
        cont = smartGuess(input("\nWould you like to learn about another class?  Yes/No: "), ["yes", "no"])
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
