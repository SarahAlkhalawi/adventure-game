import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro(monster, weapon):
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + monster + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.\n")


def cave(monster, weapon):
    # Things that happen to the player goes in the cave
    if "sward" in weapon:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before,and gotten all the good "
                    "stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        field(monster, weapon)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sward of Ogoroth!")
        print_pause("You discard your silly old dagger and take the "
                    "sward with you.")
        print_pause("You walk back out to the field.\n")
        weapon.append("sward")
        field(monster, weapon)


def house(monster, weapon):
    # Things that happen to the player in the house
    if "sward" in weapon:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens and out "
                    "steps a " + monster+".")
        print_pause("Eep! This is the " + monster + "'s house!")
        print_pause("The "+monster+" attacks you!")
        fight(monster, weapon)
    else:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens and out "
                    "steps a " + monster + ".")
        print_pause("Eep! This is the " + monster + "'s house!")
        print_pause("The " + monster + " attacks you!")
        print_pause("You feel a bit under-prepared for this, what with "
                    "only having a tiny dagger.")
        fight(monster, weapon)


def field(monster, weapon):
    # Things that happen when the player runs back to the field
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print("What would you like to do?")
    while True:
        choice = input("(Please enter 1 or 2.)\n").strip()
        if choice == '1':
            house(monster, weapon)
            break
        elif choice == '2':
            cave(monster, weapon)
            break


def fight(monster, weapon):
    # Things that happen when the player fights
    choice = input("Would you like to (1) fight or (2) run away?").strip()
    if choice == '1':
        if "sward" in weapon:
            print_pause("AS the " + monster + " moves to attack, you "
                        "unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your "
                        "hand as you brace yourself for the attack.")
            print_pause("But the " + monster + " takes on look at your "
                        "shiny new toy and runs away!")
            print_pause("You have rid the town of the " + monster + ". "
                        "You are victorious!")
            play_again()
        else:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the " + monster + ".")
            print_pause("You have been defeated!")
            play_again()
    elif choice == '2':
        print_pause("You run back into the field. Luckily, you don't "
                    "seem to have been followed.\n")
        field(monster, weapon)
    else:
        fight(monster, weapon)


def play_again():
    while True:
        response = input("Would you like to play again? (y/n)").lower().strip()
        if response == 'y':
            print_pause("Excellent! Restarting the game ...")
            play_game()
        elif response == 'n':
            print_pause("Thanks for playing! See you next time.")
            break


def play_game():
    monster = random.choice(["wicked fairie", "pirate", "dragon", "troll",
                            "gorgon"])
    weapon = []
    intro(monster, weapon)
    field(monster, weapon)


play_game()
