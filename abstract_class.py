# Смысл абстрактного класса в том, что он необходим, но его нельзя инстанциировать.
# Абстрактным классом мы накладываем обязательство на тех, кто будет от него наследовать реализовать те методы, которые мы укажем.

from abc import ABC, abstractmethod

class ChessPiece(ABC):
    # общий метод, который будут использовать все наследники этого класса
    def draw(self):
        print("Drew a chess piece")

    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def move(self):
        print("Move")
class Queen(ChessPiece):
    def move(self):
        print("Moved Queen to e2e4")

#a = ChessPiece() #TypeError: Can't instantiate abstract class ChessPiece with abstract methods move

# Мы можем создать экземпляр класса
q = Queen()
# И нам доступны все методы класса
q.draw()
q.move()
#------ Output------
#Drew a chess piece
#Moved Queen to e2e4


class Basic(ABC):
    @abstractmethod
    def hello(self):
        print("Hello from Basic class")
    def second(self):
        print("Second1")

class Advanced(Basic):
    def hello(self):
        super().hello()
        print("Enriched functionality")
    def second(self):
        super().second()
        print("Second2")
a = Advanced()
a.hello()
a.second()


#------ Output------
# Hello from Basic class
# Enriched functionality
# Second1
# Second2
