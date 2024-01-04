from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def show(self):
        pass

class Square(Shape):
    def info(self):
        print("Square has 4 sides")


class Circle(Square):

    def show(self):
        print("show circle") 
    
c = Circle()
c.info()
c.show()
