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