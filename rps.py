from enum import IntEnum
import random


class Action(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class Score():
    def __init__(self, user_score=0, computer_score=0) -> None:
        self.user_score = user_score
        self.computer_score = computer_score


def user_selection() -> IntEnum:
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


def computer_selection() -> IntEnum:
    possible_actions = [Action.ROCK, Action.PAPER, Action.SCISSORS]
    computer_action = random.choice(possible_actions)
    return computer_action


def game():
    name = input("Enter your name: ")
    score = Score()
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
                score.computer_score += 1
                pass
            else:
                print("Rock smashes scissor, you win!")
                score.user_score += 1
                pass
        elif user_action == Action.PAPER:
            if computer_action == Action.ROCK:
                print("Paper covers rock, you win!")
                score.user_score += 1
                pass
            else:
                print("Scissor cuts paper, you lose!")
                score.computer_score += 1
                pass
        else:
            if computer_action == Action.PAPER:
                print("Scissor cuts paper, you win!")
                score.user_score += 1
                pass
            else:
                print("Rock smashes scissor, you lose!")
                score.computer_score += 1
                pass

        print("\nSCORE")
        print("-----")
        print(f"{name}: {score.user_score}")
        print(f"Computer: {score.computer_score}")
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
    game()
