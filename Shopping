# Classes. Классы
class Shopping:
     def __init__(self, w, c, m = 0):
          self.what = w
          self.color = c
          self.money = m
          self.mwhere(m)

     def mwhere(self, m):
          if self.money <= 0:
              self.where = "сегодня не повезло купить"
          elif 0 < self.money < 100:
              self.where = "MANGO"
          else:
              self.where = "Michael Kors"

     def plus(self, p):
          self.plus = p
          self.money = self.money + self.plus
          #self.mwhere(self.money)
     def minus(self, mi):
          self.minus = mi
          self.money = self.money - self.minus
          #self.mwhere(self.money)

m1 = Shopping("shoes", "brown", 99)
m2 = Shopping("bag", "beige", 300)
m3 = Shopping("bag","black")

print (m1.color, m1.what,m1.where, m1.money)
print (m2.color,m2.what,m2.where)

m1.plus(150)
print (m1.what,m1.where,m1.money)

m2.minus(100)
print (m2.what,m2.where,m2.money)


'''-----------------output-----------------
brown shoes MANGO 99
beige bag Michael Kors
shoes Michael Kors 249
bag Michael Kors 200'''
