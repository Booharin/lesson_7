from abc import ABC, abstractmethod


class My_Clothes(ABC):
    @abstractmethod
    def my_name(self):
        pass

    def calculate_consumption(self):
        pass


class Clothes(My_Clothes):

    def __init__(self, my_name):
        self._my_name = my_name
        self._consumption = 0

    def my_name(self):
        print(f"My name is {self._my_name}")

    @property
    def consumption(self):
        return self._consumption

    def calculate_consumption(self):
        pass

    def __add__(self, other):
        return Clothes(self.consumption + other.consumption)


class Coat(Clothes):
    def __init__(self, my_name, my_size):
        super().__init__(my_name)
        self._my_size = my_size

    def calculate_consumption(self):
        self._consumption = self._my_size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, my_name, my_height):
        super().__init__(my_name)
        self._my_height = my_height

    def calculate_consumption(self):
        self._consumption = self._my_height * 2 + 0.3


coat = Coat("coat", 13)
coat.my_name()
coat.calculate_consumption()
print(coat.consumption)

suit = Suit("suit", 13)
suit.my_name()
suit.calculate_consumption()
print(suit.consumption)

x = coat + suit
print(x.consumption)
