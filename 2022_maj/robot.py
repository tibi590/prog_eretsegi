"""
1. Olvassa be és tárolja el a robot mozgását vezérlő szót, és annak felhasználásával oldja meg
a következő feladatokat
2. Írja ki, hogy az egyes betűkből hány darab van a szóban!
3. Írja ki a képernyőre a bekért útvonal egy lehetséges egyszerűsítését, tehát egy olyan új
parancsszót, amelyet végrehajtva a robot a lehető legkevesebb mozgással juthat el a
kiindulási pontból az eredeti parancsszónak megfelelő végső helyzetbe! 
"""

# from itertools import permutations
"""
A '#' szimbólummal ellátot kódrészletek opcionálisak

A kód a feladat által adott adatot könyvtárat használva dolgozza fel
"""

class Robot:
    def __init__(self) -> None:
        self.path:dict = {}
    def run(self):
        """
        Futtatja az alkalmazást
        """
        self.read_userinp()
        self.print_amount()
        self.new_path()
        return None
    def read_userinp(self) -> None: #task_1
        """
        Beolvassa az adatot a felhasználótol és könyvtár formájában eltárolja objektum változókénet.\n
        Ellenőrzi a beküldött adatok hitelességét, ha hibásak újra kéri azokat.
        """
        user_inp:list = list(input("Kérem a robot patrancsait: ").upper().strip())
        VALID_CHARS:list = ['E','D','K','N']
        for user_char in user_inp:
            if user_char not in VALID_CHARS:
                print("Invalid input, please try again!\nOnly use letters (E,D,K,N)")
                return self.read_userinp()
        else:
            self.path = {char:user_inp.count(char) for char in VALID_CHARS}
            return None
    def print_amount(self) -> None: #task_2
        """
        Kiiratja a betűk mennyiségét
        """
        for key in self.path:
            print(f"{key} betűk száma: {self.path[key]}")
    def new_path(self) -> None: # task3
        """
        Kiszámítja és kiiratja a legrövidebb útvonalat a felhasználó által meghatározott végponthoz.\n
        Ezt egy koordináta rendszer segítségével csinálja.
        """
        endpoint:list = [self.path['K'] - self.path['N'], self.path['E'] - self.path['D']] # -x = Ny, x = K, -y = D, y = E
        path_command = ""
        if endpoint[0] < 0:
            for i in range(abs(endpoint[0])):
                path_command += 'N'
        elif endpoint[0] > 0:
            for i in range(endpoint[0]):
                path_command += 'K'
        if endpoint[1] < 0:
            for i in range(abs(endpoint[1])):
                path_command += 'D'
        elif endpoint[1] > 0:
            for i in range(endpoint[1]):
                path_command += 'E'
        print(f"A legrövidebb út parancsszava: {path_command}")
        
        # Az összes megközelítési mód
        # |
        # V
        
        """
        print("A legrövidebb utak parancsszavai: ")
        for path in set(permutations(path_command)):
            for direction in path:
                print(direction, end='')
            print('\n', end='')
        """
        
if __name__ == '__main__':
    
    app = Robot()
    app.run()