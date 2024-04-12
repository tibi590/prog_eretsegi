# Import the randint function from the random library.
# Source for the function: https://www.w3schools.com/python/ref_random_randint.asp
from random import randint

def main() -> None:
    # 1. problem
    # Get the number of throws and convert it to an int.
    num_of_throws: int = int(input("Hany alkalommal legyen feldobas? "))

    # Initialize a dictionary for the number of wins per person.
    wins: dict = {
        'Anni': 0,
        'Panni': 0
    }

    # 2. problem
    # Loop for num_of_throws times (Loop N times).
    # Note: naming a variable '_' implies that 
    # we won't use it.
    # Don't confuse it with naming a variable
    # _x. This means the variable is private.
    for _ in range(num_of_throws):
        # The 3. problem is at the end of the throw() function.

        # Get the winner of the current round.
        winner: str = throw()

        # Record the win for the person.
        wins[winner] += 1

        # You could just use the return value of the function
        # without saving it to a variable but beacuse of readability.
        # I choose not to:
        # wins[throw()] += 1

    # 4. problem
    print(f"A jatek soran {wins['Anni']} alkalommal Anni, {wins['Panni']} alkalommal Panni nyert.")

def throw() -> str:
    # Use list comprehension to generate the 3 random numbers between 1 and 6.
    dice: list = [ randint(1, 6) for _ in range(3) ]
    # Alternative solution without list comprehension:
    # dice: list = []
    #
    # for _ in range(3):
    #     dice.append(randint(1,6))

    # Initialize an int for the sum of the dice.
    die_sum: int = sum(dice)

    # Check if the sum is more or equal to 10 and
    # set the winner for this round.
    if die_sum >= 10:
        winner: str = "Panni"
    else:
        winner: str = "Anni"

    # 3. problem
    # Print out the relevant information.
    # The '\t  ' part is important to look exactly like the example.
    # Note: '\t' means Tab.
    print(f"Dobas: {dice[0]} + {dice[1]} + {dice[2]} = {die_sum}\t  Nyert: {winner}")

    return winner

if __name__ == "__main__":
    main()
