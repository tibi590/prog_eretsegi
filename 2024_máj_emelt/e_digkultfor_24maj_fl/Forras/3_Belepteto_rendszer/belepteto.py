class Belepteto:
    """3_Belepteto_rendszer megnyitásával lett készítve a kód"""
    def __init__(self) -> None:    
        self.file:str = 'bedat.txt'
        self.students:dict = None

    def run(self) -> None:
        print(self.readData())

    def readData(self) -> dict:
        with open(self.file, 'r', encoding='utf-8') as file:
            data_lines = file.read().splitlines()
            students:dict = {
                
            }
            return data_lines

if __name__ == '__main__':
    
    app = Belepteto()
    app.run()