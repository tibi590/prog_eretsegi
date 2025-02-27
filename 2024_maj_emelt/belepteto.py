class App:
    def __init__(self) -> None:
        self.read_src:str = "bedat.txt"
        self.write_src:str = "kesok.txt"
        self.data:list = []
        self.students:list = []

    def run(self) -> None:
        # task 1
        self.readData()
        self.loadStudents()

        # task 2
        print(f"Az elso tanulo {self.data[0][1]}-kor lepett be a fokapun.")
        print(f"Az utolso tanulo {self.data[-1][1]}-kor lepett ki a fokapun.")

        # task 3
        self.writeLateStudents(self.getLateStudents())

        # task 4
        caffeteria_visitors:int = self.getStudentsByLogic("haveDone", action=3)
        print(f"A menzan aznap {len(caffeteria_visitors)} tanulo ebedelt.")

        # task 5
        library_visitors:list = self.getStudentsByLogic("haveDone", action=4)
        print(f"Aznap {len(library_visitors)} tanulo kolcsonzott a konyvtarban.")
        if len(library_visitors) > len(caffeteria_visitors):
            print("Tobben voltak, mint a menzan.")
        else:
            print("Nem voltak tobben, mint a menzan.")

        # task 6
        slackers:list = self.getStudentsByLogic("isSlacker")
        print(f"Az erintett tanulok: ")
        for slacker in slackers:
            print(slacker.id, end=" ")
        print()

        # task 7
        student_id:str = input("Egy tanulo azonositoja=").strip().upper()
        for student in self.students:
            if student.id == student_id:
                time_in_school = student.timeInSchool()
                print(f"A tanulo erkezese es tavozasa kozott {time_in_school[0]} ora es {time_in_school[1]} perc telt el.")
                break
        else:
            print("Ilyen azonositoju tanulo aznap nem volt az iskolaban.")

    def readData(self) -> None:
        with open(self.read_src, "r", encoding="utf-8") as file:
            self.data = [tuple(line.rstrip("\n").split(" ")) for line in file]

    def loadStudents(self) -> None:
        for line_data in self.data:
            new_student = Student(line_data[0])
            for existing_student in self.students:
                if new_student.id == existing_student.id:
                    existing_student.addRecord(line_data[1], int(line_data[2]))
                    break
            else:
                new_student.addRecord(line_data[1], int(line_data[2]))
                self.students.append(new_student)
                
    def getLateStudents(self) -> dict:
        EARLIEST_TIME:int = 7 * 60 + 50
        LATEST_TIME:int = 8 * 60 + 15
        late_students:dict = {}
        for student in self.students:
            for record in student.records:
                time_in_minutes:int = record.getTimeInMinutes()
                if time_in_minutes > EARLIEST_TIME and time_in_minutes <= LATEST_TIME:
                    late_students[record.time] = student.id
                    break
        return dict(sorted(late_students.items()))

    def writeLateStudents(self, late_students:dict) -> None:
        late_students:tuple = self.getLateStudents()
        with open(self.write_src, "w", encoding="utf-8") as file:
            for student in late_students:
                file.write(f"{student} {late_students[student]}\n")

    def countActions(self, action:int) -> int:
        counter:int = 0
        for student in self.students: counter += student.countAction(action)
        return counter

    def getStudentsByLogic(self, logic: str, *args, **kwargs) -> list:
        return [student for student in self.students if getattr(student, logic)(*args, **kwargs)]

class Record:
    def __init__(self, time:str, action:int) -> None:
        self.time = time
        self.action = action
        self.hour = None
        self.minute = None
        self.splitTime(time)

    def splitTime(self, time) -> None:
        splitted_time = time.split(":")
        self.hour = int(splitted_time[0])
        self.minute = int(splitted_time[1])

    def getTimeInMinutes(self) -> int:
        return self.hour * 60 + self.minute

class Student:
    def __init__(self, id:int) -> None:
        self.id:int = id
        self.records:list = []

    def addRecord(self, time:str, action:int) -> None:
        record:Record = Record(time=time, action=action)
        self.records.append(record)
    
    def haveDone(self, action:int) -> bool:
        for record in self.records:
            if record.action == action:
                return True
        return False

    def countAction(self, action:int) -> int:
        counter:int = 0
        for record in self.records: counter += 1 if record.action == action else 0
        return counter

    def isSlacker(self) -> bool:
        return self.countAction(1) > self.countAction(2)

    def getActionSorted(self, action:int) -> list:
        actions = [record for record in self.records if record.action == action]
        return sorted(actions, key=lambda record: record.time)

    def timeInSchool(self) -> tuple:
        time_min = self.getActionSorted(2)[-1].getTimeInMinutes() - self.getActionSorted(1)[0].getTimeInMinutes()
        hours = int(time_min / 60)
        minutes = time_min % 60
        return (hours, minutes)

if __name__ == "__main__":
    app = App()
    app.run()