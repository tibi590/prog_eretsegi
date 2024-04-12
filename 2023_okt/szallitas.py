def main() -> None:
    # 1. problem
    # Initialize a list for the data specified in the problem.
    weights: list = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]

    # 2. problem
    print("2. feladat")
    print(f"A targyak tomegenek osszege: {sum(weights)} Kg")

    # 3. problem
    boxes: dict = box(weights)
    print_boxes(boxes)

def box(weights: list) -> dict:
    # Initialize a dictionary for the boxes
    # with an inital value of 0: 0.
    # boxes: dict = {
    #   boxId: weight 
    # }
    boxes: dict = {0: 0}

    # Initialize an int for the boxId counter.
    boxId: int = 0

    # Iterate through the weights.
    for weight in weights:
        # Check if the current box + the current weight
        # is less than or equal to 20.
        # If true the weight gets added to the box and the loop continues.
        if boxes[boxId] + weight <= 20:
            boxes[boxId] += weight
        else:
            # Else we continue to the next box and 
            # add the current weight to it.
            boxId += 1
            boxes[boxId] = weight

    return boxes

def print_boxes(boxes: dict) -> None:
    print("\n3. feladat")

    # Initialize a string for the box weights to use in the print.
    out: str = ""

    # Iterate through the boxes and add it's weight to the out string.
    for key in boxes:
        out += f"{boxes[key]} "

    print(f"A dobozok tartalmanak tomege (kg): {out}")
    # Alternative solution in one line:
    # print(f"A dobozok tartalmanak tomege (kg): {str([ boxes[key] for key in boxes ])[1:-1].replace(',', '')}")
    # Much less readable but it's intresting.

    print(f"A szukseges dobozok szama: {len(boxes)}")

if __name__ == "__main__":
    main()
