from abc import ABC, abstractmethod
class Clothes(ABC):

    def __init__(self, parameters):
        self.parameters = parameters
        self.size = parameters
        self.height = parameters

    def __add__(self, other):
       return c.coat + s.suit

    @abstractmethod
    def important(self):
        return f"Что то важное"

class Coat(Clothes):
    @property
    def coat(self):
        c = self.size / 6.5 + 0.5
        return float(c)

    def important(self):
        pass

class Suit(Clothes):
    @property
    def suit(self):
        s = self.height * 2 + 0.3
        return float(s)

    def important(self):
        pass

c = Coat(13)
print(f"Затраты на пальто = {c.coat}")
s = Suit(50)
print(f"Затраты на костюм = {s.suit}")

print(f"Общие затраты ткани = {c.__add__(s)}")
