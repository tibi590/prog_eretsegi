from record import Record

class Student:
    def __init__(self, id:int) -> None:
        self.id:int = id
        self.records:list[Record] = []

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