from math import sqrt

class Crater:
    def __init__(self, x:float, y:float, radius:float, name:str) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.name = name # this is the PRIMARY ID

    # task 3
    def getMetrical(self) -> dict:
        return {"x": self.x, "y": self.y, "r":self.radius}

class App:
    def __init__(self) -> None:
        self.r_src:str = "felszin_tpont.txt"
        self.data:list = None
        self.craters:dict = None
        self.user_inp:str = None

    def getInput(self, text:str) -> None:
        self.user_inp = input(text)

     # task 1
    def readFile(self) -> None:
        with open(self.r_src, "r", encoding="utf-8") as file:
            self.data = [line.rstrip("\n") for line in file]

    def generateCraters(self) -> None:
        self.craters = {}
        for line in self.data:
            line_data:list = line.split("\t")
            crater = Crater(x=float(line_data[0]), y=float(line_data[1]), radius=float(line_data[2]), name=line_data[3])
            if crater.name not in list(self.craters.keys()):
                self.craters[crater.name] = crater
    
    # task 2
    def recordsAmount(self) -> int:
        return len(self.data)

    # task 5
    def getDistance(self, x1:float, y1:float, x2:float, y2:float) -> float:
        return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    # task 6
    def doesCollide(self, crater_1:Crater, crater_2:Crater) -> bool:
        return (crater_1.radius + crater_2.radius) > self.getDistance(crater_1.x, crater_1.y, crater_2.x, crater_2.y)
    
    # task 7
    def getContainers(self) -> dict:
        containers:dict = {}
        for a in self.craters:
            crater_1 = self.craters[a]
            for b in self.craters:
                crater_2 = self.craters[b]
                if crater_1.radius > crater_2.radius:
                    if self.getDistance(crater_1.x, crater_1.y, crater_2.x, crater_2.y) < (crater_1.radius - crater_2.radius):
                        containers[crater_1.name] = crater_2.name
                else:
                    if self.getDistance(crater_1.x, crater_1.y, crater_2.x, crater_2.y) < (crater_2.radius - crater_1.radius):
                        containers[crater_2.name] = crater_1.name
        return containers


    def run(self) -> None:
        # task 1
        self.readFile()
        self.generateCraters()

        # task 2
        print_data = self.recordsAmount()
        print(f"2. feladat\nA kraterek szama: {print_data}")

        #task 3
        print("3.feladat")
        self.getInput("Kerem egy krater nevet: ")
        for crater in self.craters:
            if crater == self.user_inp:
                crater_met:dict = self.craters[crater].getMetrical()
                break
        print_data = crater_met
        print(f"A(z) {self.user_inp} kozeppontja X={print_data["x"]} Y={print_data["y"]} sugara R={print_data["r"]}.")

        # task 4
        print("4. feladat")
        max_radius:float = 0.0
        max_name:str = ""
        for crater in self.craters:
            crater_met:dict = self.craters[crater].getMetrical()
            if crater_met["r"] > max_radius:
                max_radius = crater_met["r"]
                max_name = self.craters[crater].name
        print_data = (max_name, max_radius)
        print(f"Legnagyobb krater neve es sugara: {print_data[0]} {print_data[1]}")

        # task 6
        print("6. feladat")
        colliders:list = []
        self.getInput("Kerem egy krater nevet: ")
        for crater in self.craters:
            if not self.doesCollide(self.craters[crater], self.craters[self.user_inp]):
                colliders.append(crater)
        print("Nincs kozos resze: ", end="")
        print(*colliders, sep=", ", end="")
        print(".")

        # task 7
        containers:dict = self.getContainers()
        for container in containers:
            print(f"A(z) {container} krater tartalmazza a(z) {containers[container]} kratert.")


if __name__ == "__main__":
    app = App()
    app.run()