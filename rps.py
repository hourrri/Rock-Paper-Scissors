from enum import IntEnum
import random


class Action(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


def user_selection():
    while True:
        user_action = input("Rock, Paper, Scissor?: ")
        if user_action.lower() == "rock":
            user_action = Action.ROCK
            break
        elif user_action.lower() == "paper":
            user_action = Action.PAPER
            break
        elif user_action.lower() == 'scissor':
            user_action = Action.SCISSORS
            break
        else:
            print("Try again.")
    return user_action


def computer_selection():
    possible_actions = [Action.ROCK, Action.PAPER, Action.SCISSORS]
    computer_action = random.choice(possible_actions)
    return computer_action


def main():
    while True:
        user_action = user_selection()
        computer_action = computer_selection()
        print(
            f"You picked {user_action.name}, the computer chose {computer_action.name}.")
        if user_action == computer_action:
            continue
        elif user_action == Action.ROCK:
            if computer_action == Action.PAPER:
                print("Paper covers rock, you lose!")
                pass
            else:
                print("Rock smashes scissor, you win!")
                pass
        elif user_action == Action.PAPER:
            if computer_action == Action.ROCK:
                print("Paper covers rock, you win!")
                pass
            else:
                print("Scissor cuts paper, you lose!")
                pass
        else:
            if computer_action == Action.PAPER:
                print("Scissor cuts paper, you win!")
                pass
            else:
                print("Rock smashes scissor, you lose!")
                pass

        while True:
            choice = input("Would you like to play again? Y/N: ")
            if choice.lower() == "n":
                print("Thanks for playing!")
                break
            elif choice.lower() != 'y':
                print("Try again.")
                continue
            break

        if choice.lower() == "n":
            break


if "__main__" == __name__:
    main()
