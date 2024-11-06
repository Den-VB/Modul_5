# Задача "Developer - не только разработчик"
class House:
    def __init__(self, name, number_of_floors): # Начальные переменные
        self.name = name
        self.number_of_floors = number_of_floors

    def house_info(self): # вывод на экран характеристик дома
        print(f'Дом "{self.name}" имеет {self.number_of_floors} эт.')

    def go_to(self, new_floor): # Езда на лифте
        self.house_info()
        self.new_floor = new_floor
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f"Вы хотите ехать на {self.new_floor} эт.")
            print("Указанного этажа не существует, лифт не поедет!")
        else:
            print("Лифт начал движение...")
            for i in range(new_floor):
                print(i+1)
            print("Можете выходить, лифт приехал!")

 # Вводные данные
h1 = House('Уютное гнездышко', 5)
h2 = House('Небесный свод', 100)
h1.go_to(-2)
h2.go_to(7)



        