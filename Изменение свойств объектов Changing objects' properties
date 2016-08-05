# Classes. Классы
# В классе с помощью атрибутов вне функции устанавливаются свойства объектов: 
# красный цвет, круглая форма, динамическое поведение. 
# А методы могут менять эти свойства в зависимости от пожеланий тех, кто создает объекты.

class Second:
     color = "red"
     form = "circle"
     behavior = "dynamic"
     
     def changecolor(self,newcolor):
          self.color = newcolor
     def changeform(self,newform):
          self.form = newform
     def changebehavior(self,newbehavior):
          self.behavior = newbehavior   
          
obj1 = Second()
obj2 = Second()
obj3 = Second()
 
print (obj1.color, obj1.form, obj1.behavior) # вывод на экран "red circle"
print (obj2.color, obj2.form, obj2.behavior) # вывод на экран "red circle"
print (obj3.color, obj3.form, obj3.behavior)
 
obj1.changecolor("green") # изменение цвета первого объекта
obj2.changecolor("blue")  # изменение цвет второго объекта
obj2.changeform("oval")   # изменение формы второго объекта
obj3.changeform("oval")
obj3.changecolor("yellow")
obj3.changebehavior("static")

print (obj1.color, obj1.form) # вывод на экран "green circle"
print (obj2.color, obj2.form) # вывод на экран "blue oval"
print (obj3.color, obj3.form, obj3.behavior)
