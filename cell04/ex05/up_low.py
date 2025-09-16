"""swap case of a word."""

def swap_by_method(word):
    """swap case of a word."""
    return word.swapcase()

def swap_by_iteration(word):
    """swap case of a word."""
    new_word = ""
    for char in word:
        if char.islower():
            new_word += char.upper()
        else:
            new_word += char.lower()
    return new_word

def main():
    """swap case of a word."""
    word = input("Give me a word : ")
    print(f"Swap by string method : {swap_by_method(word)}")
    print(f"Swap by string iteration : {swap_by_iteration(word)}")
main()
