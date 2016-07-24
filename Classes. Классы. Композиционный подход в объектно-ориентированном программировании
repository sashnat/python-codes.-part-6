# by Nataliya.Sashnikova.
# Classes. Классы.
# Композиционный подход в объектно-ориентированном программировании.

class All: # п.1
     def __init__(self,x,y):
          self.square = x * y # используем один и тот же атрибут square
     
class Room:
     def __init__(self,x,y):
          self.square = x * y + 15 # 15м - подсобное помещение, площадь комнаты (пол), используем один и тот же атрибут square
     def tables(self,a,b,t):
          self.tables = All(a,b) # tables-объект,вычисляется площадь стола по формуле класса п.1
          self.numb_t = t # кол-во столов
     def free_space(self):
          self.freespace = self.square - self.tables.square * self.numb_t
     def printer(self):
          print ("свободная площадь равна", str(self.freespace)," кв.м")

#1. Создаем объект класса Room:
r1 = Room(10,15)
#2. Создаем в помещении столы:
r1.tables(2,1,5)
#3. Вычисляем свободное пространство:
r1.free_space()
#4. Выводим, что получилось:
r1.printer()
#В результате работы метода printer интерпретатор должен выдать что-то вроде этого:
#свободная площадь равна -- кв.м
