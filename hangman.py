#!/usr/bin/python3

import random
import sys

WORDLIST = ["linux", "gnu", "vim", "python"]
HANGMAN_GRAPHICS = [" O\n\n", " O\n |\n", " O\n/|\n", " O\n/|\\\n", " O\n/|\\\n/", " O\n/|\\\n/ \\"]

def print_hint(hint: list[str]):
    # Use escape codes to move cursor next to art for hints
    print("\033[2A\033[5C", end="")
    print(" ".join(hint), end="")
    print("\033[2B")

def print_graphic(tries: int):
    print(HANGMAN_GRAPHICS[tries])

def main():
    word = random.choice(WORDLIST)
    hint = ["_"] * len(word)
    game_running = True
    incorrect_tries = 0
    used_letters = []

    while game_running:
        print_graphic(incorrect_tries)
        print_hint(hint)

        if "_" not in hint:
            print("You win!")
            game_running = False
            break

        if incorrect_tries >= 5:
            print("You lose, the correct word was", word)
            game_running = False
            break

        letter_input = input("Letter: ")

        if letter_input in used_letters:
            print("Letter already used\n")
            continue
        else:
            used_letters.append(letter_input)

        if letter_input not in word:
            incorrect_tries += 1
            print("Nope")

        for i in range(len(hint)):
            if letter_input == word[i]:
                hint[i] = letter_input
        print()

if __name__ == "__main__":
    if "-h" in sys.argv:
        print("Simple hangman game\n")
        print("-h for help")
        print("Pass a file to use as word list")
        sys.exit()

    elif len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            # Using a set to avoid duplicates, which would affect probabilites
            WORDLIST = list(set(f.read().split()))

    main()

