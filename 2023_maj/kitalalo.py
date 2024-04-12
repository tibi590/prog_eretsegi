# Import the randint function from the random library.
# Source for the function: https://www.w3schools.com/python/ref_random_randint.asp
from random import randint

def main() -> None:
    # 1. problem
    # Initialize a list containing strings 
    # for the words specified in the problem.
    words: list[str] = ["fuvola", "csirke", "adatok", "asztal", "fogoly",
        "bicska", "farkas", "almafa", "babona", "gerinc",
        "dervis", "bagoly","ecetes", "angyal", "boglya"]
    
    # 2. problem
    # Initialize a string for the random secret word
    # using the randint() function.
    # The function returns a random number between 0 and 14
    # (length of the words list minus 1).
    secret: str = words[randint(0, len(words)-1)]

    # 3. problem
    guessing(secret)

def guessing(secret: str) -> None:
    # Initialize a string that will keep
    # track of the character that haven't been guessed.
    word: str = ""

    # Initialize an int that will count
    # the number of guesses.
    num_of_guesses: int = 0

    # Loop until the guess matches the secret word.
    while secret != word:
        # Add 1 to the guess counter.
        num_of_guesses += 1
        guess: str = input("Kerem a tippet: ")

        # Check if the input is 'stop'.
        # If true then exit from the function.
        if guess == "stop":
            return

        # Reset the word variable.
        word = ""

        # Iterate through 0 to 5.
        for i in range(6):
            # Check if the current character from 
            # the secret and guess.
            if secret[i] == guess[i]:
                # If true add current character to word.
                word += guess[i]
            else:
                # Else add '.' to word.
                word += "."

        print(f"Az eredmeny: {word}\n")

    print(f"{num_of_guesses} tippelessel sikerult kitalalni.")

if __name__ == "__main__":
    main()
