from student import Student

class App:
    def __init__(self) -> None:
        self.read_src:str = "bedat.txt"
        self.write_src:str = "kesok.txt"
        self.data:list[tuple[str, str, int]] = []
        self.students:list[Student] = []

    def run(self) -> None:
        # task 1
        self.readData()
        self.loadStudents()

        # task 2
        print("2. feladat")
        print(f"Az elso tanulo {self.data[0][1]}-kor lepett be a fokapun.")
        print(f"Az utolso tanulo {self.data[-1][1]}-kor lepett ki a fokapun.")

        # task 3
        self.writeLateStudents(self.getLateStudents())

        # task 4
        print("4. feladat")
        caffeteria_visitors:int = self.getStudentsByLogic("haveDone", action=3)
        print(f"A menzan aznap {len(caffeteria_visitors)} tanulo ebedelt.")

        # task 5
        print("5. feladat")
        library_visitors:list[Student] = self.getStudentsByLogic("haveDone", action=4)
        print(f"Aznap {len(library_visitors)} tanulo kolcsonzott a konyvtarban.")
        match len(library_visitors) > len(caffeteria_visitors):
            case True:
                p_text = "Tobben voltak, mint a menzan."
            case False:
                p_text = "Nem voltak tobben, mint a menzan."
        print(p_text)

        # task 6
        print("6. feladat")
        slackers:list[Student] = self.getStudentsByLogic("isSlacker")
        print(f"Az erintett tanulok: ")
        for slacker in slackers:
            print(slacker.id, end=" ")
        print()

        # task 7
        print("7. feladat")
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
                
    def getLateStudents(self) -> dict[str, str]:
        EARLIEST_TIME:int = 7 * 60 + 50
        LATEST_TIME:int = 8 * 60 + 15
        late_students:dict[str, str] = {}
        for student in self.students:
            for record in student.records:
                time_in_minutes:int = record.getTimeInMinutes()
                if time_in_minutes > EARLIEST_TIME and time_in_minutes <= LATEST_TIME:
                    late_students[record.time] = student.id
                    break
        return dict(sorted(late_students.items()))

    def writeLateStudents(self, late_students:dict[str, str]) -> None:
        late_students:dict[str, str] = self.getLateStudents()
        with open(self.write_src, "w", encoding="utf-8") as file:
            for student in late_students:
                file.write(f"{student} {late_students[student]}\n")

    def countActions(self, action:int) -> int:
        counter:int = 0
        for student in self.students: counter += student.countAction(action)
        return counter

    def getStudentsByLogic(self, logic: str, *args, **kwargs) -> list[Student]:
        return [student for student in self.students if getattr(student, logic)(*args, **kwargs)]