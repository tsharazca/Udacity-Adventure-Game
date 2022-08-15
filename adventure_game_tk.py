import time
import random


monster = ["Vampire", "Pontianak", "Zombie", "Banshee", "Chimera"]
monster = random.choice(monster)

location = ["clock tower", "townhall", "well", "ice house"]
location = random.choice(location)

weapon = []

# Below function allows game storyline and instructions to print on screen with delay so that it is more readable.


def print_scenario(x):
    print(x)
    time.sleep(2)


# Below storyline is introduction of the game


def introduction():
    print_scenario("You find yourself standing in an open field, filled with grass and yellow wildflowers.\n")

    print_scenario(f"Rumor has it that a {monster} is somewhere around {location}\n")

    print_scenario("And has been terrifying the village.\n")

    print_scenario("In front of you there is a house.\n")

    print_scenario("To your right there is a dark cave.\n")

    print_scenario("In your hand you are holding a trusty but not so effective dagger.\n")

    print_scenario("\n")


def monster_attack():
    print_scenario(f"""You approach the door of the house.
You are about to knock when the door opens and out steps a {monster}.
Eep! This is the {monster}'s house!
The {monster} attacks you!""")
    if "weapon" not in weapon:
        print_scenario("You feel a bit not sure for this as what you have is only a tiny dagger.\n")
        second_choice = input("""What would you like to do?
(1)fight or (2) run away?\n""")
        if second_choice == "1":
            print_scenario(f"""You do your best...
but your dagger is no match for {monster}.
You have been defeated""")
            play_again()
        elif second_choice == "2":
            print_scenario("""You run back to the field. Luckliy, you don't seem to have been followed.""")
            play()
        else:
            print_scenario("Only 1 or 2 is valid to proceed")
            monster_attack()
    else:
        third_choice = input("""What would you like to do?
(1)fight or (2) run away?\n""")
        if third_choice == "1":
            print_scenario(f"""As the {monster} moves to attack,
you unsheath your Sword.
The sword shines brightly in your hand
as you brace yourself ofr the attack.
But the {monster} takes one look at your new shiny toy and runs away!
You have rid the town of {monster}, You are victorious!""")
            play_again()
        elif third_choice == "2":
            print_scenario("""You run back to the field. Luckliy, you don't seem to have been followed.""")
            play()
        else:
            print_scenario("Only 1 or 2 is valid to proceed")
            monster_attack()


def take_weapon():
    if "weapon" in weapon:
        print_scenario("""You peer cautiously into the cave.
You've been here, and got all the good stuff.
It's just an empty cave now.""")
    else:
        print_scenario(f"""You peer cautiously into the cave.
It turns out to be only a very small cave.
Your eye catches a glint of metal behind a rock.
You have found the magical Sword!
You discard your silly old dagger and take Sword with you.
You walk back out to the field.""")
        weapon.append("weapon")
        play()

def play():
    first_choice = input("""Enter 1 to knock on the door of the house.
Enter 2 to peer into the cave.
What would you like to do?
(Please enter 1 or 2.)""")
    if first_choice == "1":
        monster_attack()
    elif first_choice == "2":
        take_weapon()


def play_again():
    playing_again = input("Would you like to play again? answer Yes as 1 or No as 2\n")
    if playing_again == "1":
        print_scenario("Restarting the Game")
        introduction()
        play()
    elif playing_again == "2":
        print_scenario("Thank you for playing, See you again!")
    else:
        print_scenario("Enter either 1 or 2 to proceed.")
        play_again()


introduction()
play()
