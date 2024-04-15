"""
A függvényeknél a '->' a visszatérési értéket jelzi,
a ':típus' a változóknál csak jelzést szolgál az olvashatóbbság kedvéért
a kód ezt ignorálja.

Ebben a példában értékbekkérésnél nem kell ellenőrizni annak helyességét, ez
az alapértelmezett a kódban, kommentben a függvényekhez oda van írva egy verzió is,
ahol leellenőrizzük azokat.

a 'self.' előtagra a program objektum orientáltáltsága miatt van szükség a függvényekbe, ha ezt
funkció orientáltan csinálnánk, ezek elhagyhatóak lennének.
"""


class Fogyokura:
    def __init__(self) -> None:
        """
        Létre hozza az osztály változókat
        """
        self.weeks:int = 0
        self.goal:float = 0
        self.weights:list = []
        self.gained_weeks:int = 0
        
    def run(self) -> None:
        """
        Futtatja az alkalmazást
        """
        self.read_goal()
        self.read_weights()
        reached_goal:list = self.reached_goal()
        if reached_goal[0] == True:
            print(f"Mari néni a(z) {reached_goal[1]}. héten érte el a célt.")
        else:
            print(f"Sajnos Mari néni nem érte el a célját.")
        self.gained_weight_weeks()
        print(f"A tömege {self.gained_weeks} esetben nőtt egyik hétről a másikra.")
        
    def read_goal(self) -> None:
        """
        Beolvassa a felhasználó által kítűzött célt
        """
        self.weeks = int(input("Hetek száma="))
        self.goal = float(input("Elérni kívánt testtömeg (kg)="))
        # try:
        #     user_weeks = int(input("Hetek száma="))
        #     user_goal = float(input("Elérni kívánt testtömeg (kg)="))
        #     self.weeks = user_weeks
        #     self.goal = user_goal
        # except ValueError:
        #     print("Error!")
        #     return self.read_weeks()
        
    def read_weights(self) -> None:
        """
        Beolvassa a heti súlyméréseit a felhasználónak
        """
        self.weights = [float(input(f"{week}. héten=")) for week in range(1, self.weeks + 1)] # Ezt nevezzük 'list comprehension'-nek, ez a python egy hasznos funkciója
        # Az alábbi módon működik [Mit rakjon a listába | Ciklus | Feltétel(ebben az esetben feltétel nélkül raktuk be a listába az elemeket)]
        # Más módon
        # for week in range(1, self.weeks + 1):
        #     user_input = float(input(f"{week}. héten="))
        #     self.weights.append(user_input)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # try:
        #     weights = [float(input(f"{week}. héten=")) for week in range(1, self.weeks + 1)]
        #     self.weights = weights
        # except ValueError:
        #     print("Error!")
        #     return self.read_weights()
        
    def reached_goal(self) -> list:
        """
        Visszaküldi egy listában, hogy a felhasználó elérte-e a célját\n
        Ha azt sikeresen megtette, a cél elérésenek napjával együtt
        """
        for index in range(len(self.weights)):
            if self.weights[index] <= self.goal:
                return [True, index + 1]    
        return [False]
    
    def gained_weight_weeks(self) -> None:
        """
        Egy változóba megállapítja, hányszor nőtt a súlya egyik hétről a másikra.
        """
        gained_weeks = 0
        for index in range(len(self.weights)):
            try:
                current_weight = self.weights[index]
                if current_weight < self.weights[index + 1]:
                    gained_weeks += 1
            except IndexError:
                break
        self.gained_weeks = gained_weeks
                
if __name__ == '__main__':
    app = Fogyokura()
    app.run()