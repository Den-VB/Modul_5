# Задача "Магические здания"
class House:
    def __init__(self, name, number_of_floors): # Начальные переменные
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self): # вывод на экран характеристик дома
        return self.number_of_floors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int) and isinstance(self.number_of_floors, int):
            return House(self.name, self.number_of_floors + value)
        else:
            print("Усе пропало, шеф!")
            return self.number_of_floors

    def __radd__(self, value):
        if isinstance(value, int) and isinstance(self.number_of_floors, int):
            return House(self.name, self.number_of_floors + value)
        else:
            print("Усе пропало, шеф!")
            return self.number_of_floors


 # Вводные данные
h1 = House('Уютное гнездышко', 10)
h2 = House('Небесный свод', 20)

print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2)