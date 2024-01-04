from abc import ABC, abstractmethod

class Armed_Forces(ABC):
    
    def gun(self):
        print("Gun : AK47")

    @abstractmethod
    def area(self):
        pass

class Army(Armed_Forces):
    def area(self):
        print("Area : Land")

class Air_Force(Armed_Forces):
    def area(self):
        print("Area : Air")

class Navy(Armed_Forces):
    def area(self):
        print("Area : Sea")

Army().gun()
Army().area()
print()
Air_Force().gun()
Air_Force().area()
print()
Navy().gun()
Navy().area()