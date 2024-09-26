def main() -> None:
    # 1. problem
    lines: list[str] = read_file()

    # 2. problem
    print("2. feladat")
    print(f"A felajanlasok szama: {len(lines[1:])}")

    # 3. problem
    print("\n3. feladat")
    print(f"A bejarat mindket oldalan ultetok: {get_entrance_planters(lines[1:])}")

    # 4. problem
    print("\n4. feladat")
    pot_num: int = int(input("Adja meg az agyas sorszamat! "))
    check_pot(pot_num, lines[1:], int(lines[0]))

def read_file() -> list[str]:
    with open("./forras/felajanlas.txt", "r") as f:
        lines: list[str] = f.read().splitlines()

    return lines

def get_entrance_planters(lines: list[str]) -> str:
    planters: str = ""

    for i, line in enumerate(lines):
        pot1, pot2 = line.split(" ")[0:2]

        if int(pot1) > int(pot2):
            planters += f"{i+1} "

    return planters

def check_pot(pot_num: int, lines: list[str], num_of_pots: int) -> None:
    count: int = 0
    final_color: str = ""
    all_colors: str = ""

    for line in lines:
        pot1, pot2, color = line.split(" ")

        pot1 = int(pot1)
        pot2 = int(pot2)

        if pot1 < pot2:
            if pot1 <= pot_num and pot_num <= pot2:
                if not final_color:
                    final_color = color

                if color not in all_colors:
                    all_colors += f"{color} "

                count += 1
        else:
            if pot1 <= pot_num <= num_of_pots or 0 <= pot_num <= pot2:
                if not final_color:
                    final_color = color

                if color not in all_colors:
                    all_colors += f"{color} "

                count += 1

    print(f"ajanlasok szama: {count}")
    if final_color:
        print(f"A virag agyas szine, ha csak az elso ultet: {final_color}")
    else:
        print("Ezt az agyast nem ultetik be!")

    if all_colors:
        print(f"A virag agyas szinei: {all_colors}")

if __name__ == "__main__":
    main() 
