from hangman.game import *


def prompt_guess() -> str:
    user_guess = input("enter your guess: ")
    return user_guess

def print_status(state: dict) -> None:
    print(state["max_tries"] - len(state["guessed"]))
    print(state["guessed"])
    print(render_display(state))

def print_result(state: dict) -> None:
    if is_won(state):
        print("you ween")
    else:
        print("you lose")
    render_summary(state)
