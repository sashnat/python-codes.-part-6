# Classes. Классы. Наследование в ООП. 
# Напишите программу, где класс «геометрические фигуры» (figure) 
# содержит свойство color с изначальным значением white и метод для изменения цвета фигуры, 
# а его подклассы «овал» (oval) и «квадрат» (square) содержат методы __init__ 
# для задания начальных размеров объектов при их создании.....

class Figure:
     def __init__(self,w="white"):
         self.color = w
     def changecolor(self,ch):
         self.chcolor = ch

class Oval(Figure):
     def __init__(self,r,x,y):
         self.radius = r
         self.ox = x
         self.oy = y
         super().__init__()
     def out(self):
         print (self.radius,self.ox,self.oy)


class Square(Figure):
     def __init__(self,w,h):
         self.widht = w
         self.height = h
         super().__init__()
     def howsides(self,n):
          self.sides = n
          if not self.sides == 4:
               print ("It is not a sguare")
          else:
               print ("It is a sguare")

     def outsides(self):
          print (self.sides)

x = Figure("red")
print(x.color)

o = Oval(5,0,0)
o.out()
o.changecolor("black")
print(o.chcolor, o.radius)

s = Square(8,8)
s.howsides(4)
s.outsides()
s.changecolor("grey")
print(s.chcolor, s.widht, s.height)

'''
-------------------------------output--------------------------
red
5 0 0
black 5
It is a sguare
4
grey 8 8
'''
