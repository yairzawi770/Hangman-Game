import random
from hangman.io import prompt_guess
from data.words_collection import words
from hangman.game import *
from hangman.words import choose_secret_word


def play(words: list[str], max_tries: int = 6) -> None:
    secret_word = choose_secret_word(words)
    state = init_state(secret_word, max_tries)

    while not is_lost(state) and not is_won(state):
        print(render_display(state))
        print(state["secret"])
        char = prompt_guess()
        is_valid_char, msg = validate_guess(char,state["guessed"])
        print(msg)
        if is_valid_char:
            apply_guess(state,char)
    summary = render_summary(state)
    print(summary)
    print(state)

if __name__ == "__main__":
    play(words)
