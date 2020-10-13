import string


def is_pangram(sentence: str):
    set_alphabet = set("abcdefghijklmnopqrstuvwxyz")
    set_used = set()
    for char in sentence.lower():
        if 97 <= ord(char) <= 122:
            set_used.add(char)
    if set_used == set_alphabet:
        return True
    return False