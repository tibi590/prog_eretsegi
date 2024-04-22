
class Taj:
    def __init__(self) -> None:
        self.taj:int = None
        self.check:int = None
        self.mult_sum:int = None
    
    def run(self) -> None:
        self.taj = self.readTaj()
        self.check = self.getCheck()
        self.mult_sum = self.multSum()

        print(f"Az ellenőrzőszámjegy: {self.check}")
        if self.matchCheck():
            print("Helyes a szám!")
        else:
            print("Hibás szám!")

    def matchCheck(self) -> bool:
        if self.mult_sum % 10 == self.check:
            return True
        else:
            return False
        
    def multSum(self) -> int:
        val_sum = 0
        for i in range(len(self.taj)):
            if i + 1 % 2 == 0:
                val_sum += self.taj[i] * 7
            else:
                val_sum += self.taj[i] * 3
        return val_sum

    def getCheck(self, taj:int) -> int:
        return taj[-1]
    
    def readTaj(self) -> int:
        return int(input("Kérem a TAJ-számot: "))
        # user_inp = 0
        # while len(user_inp) != 7:
        #     try:
        #         user_inp = int(input("Kérem a TAJ-számot: "))
        #     except ValueError:
        #         return self.readTaj()
        # return user_inp

if __name__ == '__main__':

    app = Taj()
    app.run()