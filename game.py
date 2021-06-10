from random import choice
# pip3 install colorama
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
# "Gallows"
# "Classic game where the computer picks a random word."
# "Player tries to guess its individual letters."
# "If player does not guess the word, the game ends with a man on the gallows."

HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   -+-
     | 
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | 
     |   | 
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | |
     |   | |
     |  
    ----------
    """)


WORDS = ['GRANIT', 'KECZUP' ,'KOMPAS',
'KRUSZYNA', 'WHISKY' ,'WIĘZIENIE', 'ODWAGA']

pick = choice(WORDS)   #pick one word form WORDS
MAX_WRONG = len(HANGMAN)-1   #max fail attempts
so_far = "-" * len(pick) # correct letters other '-'
wrong = 0
used_letters = []

print("Welcom in game")
while wrong != MAX_WRONG and so_far != pick:
    print(f"{Fore.RED}{HANGMAN[wrong]}")
    print(f"{Fore.BLACK}{Back.BLUE}Used letters: {used_letters}")
    print(f"{Fore.BLACK}{Back.YELLOW}Right now word looks like this: {so_far}")

    guess = input(f"{Fore.LIGHTBLUE_EX}Enter a letter: ")
    guess = guess.upper()

    while guess in used_letters:
        print("You already used that letter")
        guess = input(f"{Fore.LIGHTBLUE_EX}Enter a letter: ")
        guess = guess.upper()
    used_letters.append(guess)

    if guess in pick:
        print(f"{Fore.GREEN}This letter is in word")

        new = ""
        for i in range(len(pick)):
            if guess == pick[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print(f"{Fore.RED}This letter not in word")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print(f"{Fore.LIGHTRED_EX}You lose")
else:
    print(f"{Fore.LIGHTGREEN_EX}You win")

print(f"The mysterious word is {pick}")