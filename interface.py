from abc import ABC, abstractmethod
class EmployeeStorage(ABC):

    @abstractmethod
    def GetData(self):
        pass

class EmployeeDB(EmployeeStorage):

    def GetData(self):
        # gets from database
        return ["Hasan", "Ali", "Arash", "Ahmad"]
    
class EmoloyeeRestApi(EmployeeStorage):

    def GetData(self):
        # gets from rest api
        return ["Hasan", "Ali", "Arash", "Ahmad"]

class EmployeeFile(EmployeeStorage):
        
    def GetData(self):
        # gets from rest api
        return ["Hasan", "Ali", "Arash", "Ahmad"]
    
class Printer:
    def __init__(self, db:EmployeeStorage):
        if(isinstance(db, EmployeeStorage)):
            self.employees = db
        else:
            raise TypeError()
        

    def Display(self):
        result = self.employees.GetData()

        for item in result:
            print(item)

printer = Printer(EmployeeFile())

printer.Display()