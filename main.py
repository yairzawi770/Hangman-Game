import random
from hangman.io import prompt_guess
from data.words_collection import words
from hangman.game import *
from hangman.words import choose_secret_word


def play(words: list[str], max_tries: int = 6) -> None:
    secret_word = choose_secret_word(words)
    state = init_state(secret_word, max_tries)

    while not is_lost(state) or not is_won(state):
        print(render_display(state))
        print(state["secret"])
        print((is_won(state)))
        print(state["display"])
        char = prompt_guess()
        is_valid_char, msg = validate_guess(char,state["guessed"])
        print(msg)
        if is_valid_char:
            apply_guess(state,char)
        print(state)
        # while char in state["guessed"]:
        #     print("give me a new guess again")
        #     char = prompt_guess()
        #
        # is_apply = apply_guess(state, char)
        # if is_apply:
        #     print("you right")

if __name__ == "__main__":
    play(words)
