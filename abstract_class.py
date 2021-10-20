# Смысл абстрактного класса в том, что он необходим, но его нельзя инстанциировать.
# Абстрактным классом мы накладываем обязательство на тех,
# кто будет от него наследовать реализовать те методы, которые мы укажем.

from abc import ABC, abstractmethod

class Basic(ABC):
    @abstractmethod
    def hello(self):
        print("Hello from Basic class_1")
    @abstractmethod
    def second(self):
        print("Hello from Basic class_second_method_1")
    @abstractmethod
    def third(self):
        pass
    # @abstractmethod
    # def forth(self):
    #     print("Hello from Basic class_forth_1")

class Advanced(Basic):
    def hello(self):
        super().hello()
        print("Enriched functionality_1")
    def second(self):
        #super().second()
        print("Second_1")
    def third(self):
        super().third()
        print("Third_1")


a = Advanced()
a.hello()
a.second()
a.third()
#a.forth() TypeError: Can't instantiate abstract class Advanced with abstract methods forth
# класс Advanced должен обязательно иметь имплементацию метода forth, поскольку это задекларировано в родительском классе Base:

#-------------------Output--------------
# Hello from Basic class_1
# Enriched functionality_1
# Second_1
# Third_1
