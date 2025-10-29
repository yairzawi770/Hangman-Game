from data.words_collection import hebrew_alphabet


def init_state(secret: str, max_tries: int) -> dict:
    length = "_"
    under_score = [length] * len(secret)
    status = {
        "secret": secret,  # המילה הסודית
        "display": under_score,  # רשימת תווים לתצוגה, "_"
        "guessed": set(),  # אותיות שנוחשו
        "wrong_guesses": 0,  # כמה טעויות בוצעו
        "max_tries": max_tries  # מגבלה
    }
    return status

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if len(ch) != 1:
        return False, "Only one letter."
    if ch not in hebrew_alphabet:
        return False, 'not valid, only Hebrew letters.'
    if ch in guessed:
        return False, 'the letter is alredy guessed.'
    else:
        return True, 'keep going'

def apply_guess(state: dict, ch: str) -> bool:
    state["guessed"].add(ch)
    if ch not in state["secret"]:
        print("You guessed wrong.")
        state["wrong_guesses"]+=1
        return False
    else:
        for index,char in enumerate(state["secret"]):
            if char == ch:
                state["display"][index] = ch
        return True


def is_won(state: dict) -> bool:
    if "_" not in state["display"]:
        return True
    else:
        return False

def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    else:
        return False

def render_display(state: dict) -> str:
    return " ".join(state["display"])

def render_summary(state: dict) -> str:
    return state["secret"] , state["guessed"]

