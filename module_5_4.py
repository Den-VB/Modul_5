# Задача "История строительства":
class House:
    houses_history = []

    def __new__(cls, *args):
        house_name = args[0]
        cls.houses_history.append(house_name)
        return super().__new__(cls)
    
    def __init__(self, name, number_of_floors): # Начальные переменные
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'Дом "{self.name}" снесён, но память о нем не погибла')

 # Вводные данные
h1 = House('Уютное гнездышко', 10)
print(House.houses_history)
h2 = House('Небесный свод', 20)
print(House.houses_history)
h3 = House('Курочка Ряба', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)