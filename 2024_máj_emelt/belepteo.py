class App:
    def __init__(self) -> None:
        self.read_src:str = "bedat.txt"
        self.write_src:str = "kesok.txt"
        self.data:list = []
        self.students:dict = {}

    def run(self) -> None:
        # task 1
        self.readData()
        self.loadStudents()

        # task 2
        first_arrival:tuple =self.getDataOfIdnex(0)
        last_arrival:tuple =self.getDataOfIdnex(-1)
        print(f"Az elso tanulo {first_arrival[1]}-kor lepett be a fokapun.")
        print(f"Az utolso tanulo {last_arrival[1]}-kor lepett ki a fokapun.")

        # task 3
        self.writeLateStudents(self.getLateStudents())

        # task 4
        lunches = self.getLunches()
        print(f"A menzan aznap {lunches} tanulo ebedelt.")

        # task 5
        library_students:list = self.getStudentsInLibrary()
        print(f"Aznap {len(library_students)} tanulo kolcsonzott a konyvtarban.")
        if len(library_students) > lunches:
            print("Tobben voltak, mint a menzan.")
        else:
            print("Nem voltak tobben, mint a menzan.")

        # task 6
        slackers:list = self.getSlackers()
        print(f"Az erintett tanulok: ")
        for slacker in slackers:
            print(slacker.id, end=" ")

    # task 1
    def readData(self) -> None:
        with open(self.read_src, "r", encoding="utf-8") as file:
            self.data = [line.rstrip("\n") for line in file]

    def loadStudents(self) -> None:
        for line in self.data:
            line_data = line.split(" ")
            student = Student(line_data[0])
            if student.id not in list(self.students.keys()):
                self.students[student.id] = student
            self.students[student.id].addRecord(line_data[1], int(line_data[2]))

    # task 2
    def getDataOfIdnex(self, index:int) -> tuple:
        return tuple(self.data[index].split(" "))

    # task 3
    def getLateStudents(self) -> dict:
        EARLIEST_TIME:int = 7 * 60 + 50
        LATEST_TIME:int = 8 * 60 + 15
        late_students:dict = {}
        for student in self.students:
                for record in self.students[student].records:
                    time_in_minutes = record.getTimeInMinutes()
                    if time_in_minutes > EARLIEST_TIME and time_in_minutes <= LATEST_TIME:
                        late_students[student] = record.time
                        break
        return late_students

    def writeLateStudents(self, late_students:dict) -> None:
        late_students:tuple = self.getLateStudents()
        with open(self.write_src, "w", encoding="utf-8") as file:
            for student in late_students:
                file.write(f"{late_students[student]} {student}\n")

    # task 4
    def getLunches(self) -> int:
        lunches:int = 0
        for student in self.students:
            for record in self.students[student].records:
                if record.action == 3: 
                    lunches += 1
                    break
        return lunches

    # task 5
    def getStudentsInLibrary(self) -> list:
        return [student for student in self.students.values() if student.beenInLibrary()]

    # task 6
    def getSlackers(self) -> list:
        return [student for student in self.students.values() if student.isSlacker()]


class Record:
    def __init__(self, time:str, action:int) -> None:
        self.time = time
        self.action = action
        self.hours = None
        self.minutes = None
        self.splitTime()

    def splitTime(self) -> None:
        splitted_time = self.time.split(":")
        self.hours = int(splitted_time[0])
        self.minutes = int(splitted_time[1])

    def getTimeInMinutes(self) -> int:
        return self.hours * 60 + self.minutes


class Student:
    def __init__(self, id:int) -> None:
        self.id = id
        self.records:list = []

    def addRecord(self, time:str, action:int) -> None:
        record:Record = Record(time=time, action=action)
        self.records.append(record)

    def beenInLibrary(self) -> bool:
        for record in self.records:
            if record.action == 4:
                return True
        return False

    def actionCounter(self, action:int) -> int:
        counter:int = 0
        for record in self.records:
            if record.action == action:
                counter += 1
        return counter

    def isSlacker(self) -> bool:
        if self.actionCounter(1) > self.actionCounter(2):
            return True
        return False

if __name__ == "__main__":
    app = App()
    app.run()