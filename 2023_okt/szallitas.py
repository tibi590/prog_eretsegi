def main() -> None:
    # 1. problem
    # Initialize a list for the data specified in the problem.
    weights: list[int] = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]

    # 2. problem
    print("2. feladat")
    print(f"A targyak tomegenek osszege: {sum(weights)} Kg")

    # 3. problem
    boxes: list[int] = box(weights)
    print_boxes(boxes)

def box(weights: list[int]) -> list[int]:
    # Initialize a list containing integers for the boxes
    # with an initial value of 0 (The weight of the first box).

    # Note: In the boxes list every element represents
    # a new box and the element's value represents it's weight.
    # Here I create the first box with an initial weight of 0.
    boxes: list[int] = [0]

    # Iterate through the weights
    for weight in weights:
        # Check if the current box plus the current weight
        # is less than or equal to 20.
        if boxes[-1] + weight <= 20:
            # If true then add the current weight 
            # to the current box.
            boxes[-1] += weight
        else:
            # Else create a new box and 
            # with the current weight.
            boxes.append(weight)

    return boxes

def print_boxes(boxes: list[int]) -> None:
    print("\n3. feladat")

    # Initialize a string for the box weights to use in the print.
    out: str = ""

    # Iterate through the boxes and add it's weight to the out string.
    for box in boxes:
        out += f"{box} "

    print(f"A dobozok tartalmanak tomege (kg): {out}")
    # Alternative solution in one line:
    # print(f"A dobozok tartalmanak tomege (kg): {str([ boxes[key] for key in boxes ])[1:-1].replace(',', '')}")
    # Much less readable but it's intresting.

    print(f"A szukseges dobozok szama: {len(boxes)}")

if __name__ == "__main__":
    main()
