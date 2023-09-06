import time
import random

shiny_tool = ["The Sword of Ogoroth",
              "the deadly poleaxe", "the chinese knife"]
item = random.choice(shiny_tool)


def pause(message, delay=2):
    print(message)
    time.sleep(delay)


def valid(s, op1, op2):
    q = input(s).lower()
    if q == op1:
        return q
    elif q == op2:
        return q
    else:
        pause("invalid input,re-enter please")
        valid(s, op1, op2)


def intro():
    pause("You find yourself standing in an open field,"
          "filled with grass and yellow wildflowers.\n")
    pause("Rumor has it that a wicked fairie is somewhere around here,"
          "and has been terrifying the nearby village.\n")
    pause("In front of you is a house.")
    pause("To your right is a dark cave.")
    pause("In your hand you hold your trusty (but not very effective) dagger.")


def house(tools, enemy):
    pause("You approach the door of the house.")
    pause(f"You are about to knock when "
          f"the door opens and out steps a {enemy}.")
    pause(f"Eep! This is the {enemy}'s house!")
    pause(f"The {enemy} attacks you!")
    if "tiny dagger" in tools:
        pause("You feel a bit under-prepared for this,"
              "what with only having a tiny dagger.")


def cave(tools, item):
    if item in tools:
        pause("You peer cautiously into the cave.")
        pause("You've been here before, and gotten all the good stuff."
              "It's just an empty cave now.")
        pause("You walk back out to the field.")
        field(tools)
    else:   # if the tool is not provided

        pause("You peer cautiously into the cave.")
        pause("It turns out to be only a very small cave.")
        pause("Your eye catches a glint of metal behind a rock.")
        pause(f"You have found  {item}!")
        pause(f"You discard your silly old dagger and take {item} with you.")
        pause("You walk back out to the field.")
        tools.append(item)
        field(tools)


def fight(tools, item, enemy):
    if item in tools:
        pause(f"As the {enemy} moves to attack, you unsheath your new sword."
              f"{item} shines brightly in your"
              "hand as you brace yourself for the attack.")
        pause(f"But the {enemy} takes one look"
              "at your shiny new toy and runs away!")
        pause(f"You have rid the town of the {enemy}. You are victorious!")
        restart()

    else:  # if the tool is not provided user get deafeted
        pause("You do your best...")
        pause(f"but your dagger is no match for the {enemy}.")
        pause("You have been defeated!")
        restart()


def field(tools):
    enemy_list = ["dragon", "gorgon", "monster"]
    enemy = random.choice(enemy_list)
    pause("Enter 1 to knock on the door of the house. ")
    pause("Enter 2 to peer into the cave. ")
    action = valid("What would you like to do?\n"
                   "(Please enter 1 or 2).\n", "1", "2")
    if "1" == action:
        house(tools, enemy)
    elif "2" == action:
        cave(tools, item)

    second_action = valid("Would you like to (1)"
                          "fight or (2) run away?\n", "1", "2")
    if "1" == second_action:
        fight(tools, item, enemy)
    elif "2" == second_action:
        pause("You run back into the field. Luckily,"
              " you don't seem to have been followed.")
        field(tools)


def restart():
    pause("GAME OVER")
    play = valid("Would you like to play again? (y/n)\n", "y", "n")
    if "y" == play:
        pause("Excellent! Restarting the game ...")
        global item
        item = random.choice(shiny_tool)
        game()
    elif "n" == play:
        pause("Thanks for playing! See you next time.")
        exit()
    else:
        trash = input("to reset press enter "
                      "then re-enter your answer, enjoy the game! :)")
        restart()


def game():
    tools = ["trusty dagger"]
    intro()
    field(tools)


game()
