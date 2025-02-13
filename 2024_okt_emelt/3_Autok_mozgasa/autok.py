"""
tobbszor is lefut foloslegesen a rekordokon vegigfuto loop (O(n*k)) idokomplexitasu
"""

class App:
    def __init__(self) -> None:
        self.r_src:str = "jeladas.txt"
        self.w_src:str = "ido.txt"
        self.data:list = None
        self.cars = None
        self.user_input = None

    def loadData(self) -> None:
        with open(self.r_src, "r", encoding="utf-8") as file:
            self.data = [line.rstrip("\n") for line in file]

    def loadCars(self) -> None:
        self.cars:dict = {}
        for line in self.data:
            line_data = line.split("\t")
            car = Car(line_data[0])
            if car.code not in list(self.cars.keys()):
                self.cars[car.code] = car
            self.cars[car.code].addRecord(hour=int(line_data[1]), minute=int(line_data[2]), speed=int(line_data[3]))

    def getInput(self, text) -> None:
        self.user_input = input(text)

    def run(self) -> None:
        self.loadData()
        self.loadCars()

        # task 2
        print_data = self.getSignal(record_index=-1)
        print(f"Az utolso jeladas idopontja {print_data["time"][0]}:{print_data["time"][1]}, a jarmu rendszama {print_data["code"]}")

        # task 3
        print_data = (self.getSignal(record_index=0)["code"], self.getCarTimes(self.getSignal(record_index=0)["code"]))
        print(f"Az elso jarmu: {print_data[0]}\nJeladasainak idopontjai: ", end="")
        for time in print_data[1]:
            print(f"{time[0]}:{time[1]} ", end="")
        print()

        # task 4
        self.getInput("Kerem, adja meg az orat: ")
        hour = int(self.user_input)
        self.getInput("Kerem, adja meg a percet: ")
        minute = int(self.user_input)
        print_data = self.getSiglnasAmount(hour=hour, minute=minute)
        print(f"A jeladasok szama: {print_data}")

        # task 5
        max_speed:int = self.getHighestSpeed()
        cars_at_speed:list = self.getCarAtSpeed(max_speed)
        print_data = (max_speed, cars_at_speed)
        print(f"A legnagyobb sebesseg km/h: {print_data[0]}")
        print(f"A járművek: ", end="")
        print(*print_data[1])

        # task 6
        self.getInput("Kerem, adja meg a rendszamot: ")
        car_code = self.user_input
        travel_records:list = self.cars[car_code].getTravelRecord()
        print_data = travel_records
        for record in print_data:
            print(f"{record[0]} {record[1]} km")

        # task 7
        self.writeRecordsFile()


    # task 2
    def getSignal(self, record_index:int) -> dict:
        line_data:str = self.data[record_index].split("\t")
        return {"code":line_data[0], "time": (line_data[1], line_data[2])}
    
    # task 3
    def getCarTimes(self, code:str) -> list:
        return [(record["hour"], record["minute"]) for record in self.cars[code].records]
    
    # task 4
    def getSiglnasAmount(self, hour, minute) -> int:
        signals_given:int = 0
        for car in self.cars:
            for record in self.cars[car].records:
                if record["hour"] == hour and record["minute"] == minute:
                    signals_given += 1
        return signals_given
    
    # task 5
    def getHighestSpeed(self) -> int:
        max_speed:int = 0
        for car in self.cars:
            for record in self.cars[car].records:
                if record["speed"] > max_speed:
                    max_speed = record["speed"]
        return max_speed
    
    def getCarAtSpeed(self, speed:int) -> list:
        car_codes:list = []
        for car in self.cars:
            for record in self.cars[car].records:
                if record["speed"] == speed:
                    car_codes.append(self.cars[car].code)
                    break
        return car_codes

    # task 7
    def writeRecordsFile(self) -> None:
        with open(self.w_src, "w", encoding="utf-8") as file:
            for car_code in self.cars:
                f_hour = self.cars[car_code].records[0]["hour"]
                f_minute = self.cars[car_code].records[0]["minute"]
                l_hour = self.cars[car_code].records[-1]["hour"]
                l_minute = self.cars[car_code].records[-1]["minute"]
                file.write(f"{car_code} {f_hour} {f_minute} {l_hour} {l_minute}\n")

class Car:
    def __init__(self, code) -> None:
        self.code:str = code
        self.records:list = []

    def addRecord(self, hour:str, minute:str, speed:int) -> None:
        record:dict = {
            "hour": hour,
            "minute": minute,
            "speed": speed
        }
        self.records.append(record)

    # task 6
    def getTravelRecord(self) -> dict:
        sum_km:float = 0.0
        travel_records:list = []
        for index in range(len(self.records)):
            time = f"{self.records[index]["hour"]}:{self.records[index]["minute"]}"
            travel_records.append((time, round(sum_km, 1)))
            try:
                sum_km += (self.getRecordMinuteDiff(indexes=(index, index + 1)) / 60) * self.records[index]["speed"]
            except IndexError:
                break
        return travel_records

    def getRecordMinuteDiff(self, indexes:tuple) -> int:
        record_a_hours:int = self.records[indexes[0]]["hour"]
        record_a_minutes:int = self.records[indexes[0]]["minute"]
        record_b_hours:int = self.records[indexes[1]]["hour"]
        record_b_minutes:int = self.records[indexes[1]]["minute"]
        return (record_b_hours * 60 + record_b_minutes) - (record_a_hours * 60 + record_a_minutes)


if __name__ == "__main__":
    app = App()
    app.run()