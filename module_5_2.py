# Задача "Магические здания"
class House:
    def __init__(self, name, number_of_floors): # Начальные переменные
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self): # вывод на экран характеристик дома
        return self.number_of_floors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}'



 # Вводные данные
h1 = House('Уютное гнездышко', 5)
h2 = House('Небесный свод', 100)

print(h1)
print(h2)

print(len(h1))
print(len(h2))