def main() -> None:
    # 1. problem 
    prompt: str = input("Kerem a robot parancsait: ")

    # 2. problem
    print_chars(prompt)

    # 3. problem
    route: str = update_route(prompt)
    print(f"Egy legrovidebb ut parancsszava: {route}")

def print_chars(prompt: str) -> None:
    # Initialize a dictionary for the directions.
    chars = {
        'E': 0,
        'D': 0,
        'K': 0,
        'N': 0
    }

    # Iterates through the prompt and 
    # adds 1 to the current character.
    for char in prompt:
        chars[char] += 1;

    # Print out the number of the current character.
    for key in chars:
        print(f"{key} betuk szama: {chars[key]}")

def update_route(prompt: str) -> str:
    # Initialize a dictionary for the final position. 
    coordinate: dict = {
        'x': 0,
        'y': 0
    }

    # Iterate through the prompt and change the coordinate
    # based on the current character (direction).
    for char in prompt:
        match char:
            case 'E':
                coordinate['y'] += 1;
            case 'D':
                coordinate['y'] -= 1;
            case 'K':
                coordinate['x'] += 1;
            case 'N':
                coordinate['x'] -= 1;

    # Initialize a string for the new route.
    route: str = ""

    # Calculate the new route based on the final position.
    # Checks if y coordinate is positive.
    if coordinate['y'] > 0:
        # If true then append the 'E' character y times.
        route += 'E'*coordinate['y']
    else:
        # Else append the 'D' character abs(y) times.
        route += 'D'*abs(coordinate['y'])

    # Checks if x coordinate is positive.
    if coordinate['x'] > 0:
        # If true then append the 'K' character x times. 
        route += 'K'*coordinate['x']
    else:
        # Else append the 'N' character abs(x) times. 
        route += 'N'*abs(coordinate['x'])

    return route

if __name__ == "__main__":
   main() 
