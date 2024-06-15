# class Building:
#     def __init__(self, height, width, square, floor):
#         self.__height = height
#         self.__width = width
#         self.__square = square
#         self.__floor = floor
#
#
#     def get_height(self):
#         return self.__height
#     def set_height(self, height):
#         self.__height = height
#     def get_width(self):
#         return self.__width
#     def set_width(self, width):
#         self.__width = width
#     def get_square(self):
#         return self.__square
#     def set_square(self, square):
#         self.__square = square
#     def get_floor(self):
#         return self.__floor
#     def set_floor(self, floor):
#         self.__floor = floor
#
#     def get_info(self):
#         print(f"height: {self.get_height()}/n"
#               f"width: {self.get_width()}/n"
#               f"square: {self.get_square()}/n"
#               f"floor: {self.get_floor()}/n")
#
# class School(Building):
#     def __init__(self, height, width, square, floor, gym, library):
#         super().__init__(self, height, width, square, floor, gym, library)
#         self.__gym = gym
#         self.__library = library
#
#     def get_gym(self):
#         return self.__gym
#     def set_gym(self):
#         self.__gym = gym
#
#     def get_library(self):
#         return self.__library
#     def set_library(self):
#         self.__library = library
#
#     def get_info(self):
#         super().get_info()
#         print(f"gym: {self.get_gym()}/n"
#               f"library: {self.get_library()}/n")
#
#
# class House(Building):
#     def __init__(self, height, width, square, floor, garag):
#         super().__init__(self, height, width, square, floor, garag)
#         self.__garag = garag
#
#     def get_garag(self):
#         return self.__garag
#     def set_garag(self):
#         self.__garag = garag
#
#     def get_info(self):
#         super().get_info()
#         print(f"garag: {self.get_garag()}/n")
#
# school = School("30m", "20m", "600", "yes", "yes", "yes")
# house = House("10", "20", "300", "2", "yes")
#
# school.get_info()
# print(school)
# house.get_info()
# print(house`    )
# Базовый класс для всех транспортных средств
class Vehicle:
    def __init__(self, brand, model, year, max_speed, color):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__max_speed = max_speed
        self.__color = color

    def display_info(self):
        print(f"Марка: {self.__brand}, Модель: {self.__model}, Год: {self.__year}, Макс. скорость: {self.__max_speed} км/ч, Цвет: {self.__color}")

class Car(Vehicle):
    def __init__(self, brand, model, year, max_speed, color, engine_volume):
        super().__init__(brand, model, year, max_speed, color)
        self.engine_volume = engine_volume
        self.wheels = 4
        self.doors = 4
        self.seats = 5
        self.fuel_type = "Бензин"

class Bicycle(Vehicle):
    def __init__(self, brand, model, year, max_speed, color, bike_type):
        super().__init__(brand, model, year, max_speed, color)
        self.bike_type = bike_type
        self.wheels = 2
        self.brakes_type = "Дисковые"
        self.gears = 21
        self.frame_material = "Алюминий"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, max_speed, color, engine_volume):
        super().__init__(brand, model, year, max_speed, color)
        self.engine_volume = engine_volume
        self.wheels = 2
        self.seats = 2
        self.fuel_type = "Бензин"
        self.helmet_included = True

class Truck(Vehicle):
    def __init__(self, brand, model, year, max_speed, color, cargo_capacity):
        super().__init__(brand, model, year, max_speed, color)
        self.cargo_capacity = cargo_capacity
        self.wheels = 6
        self.doors = 2
        self.fuel_type = "Дизель"
        self.trailer_hook = True

class Bus(Vehicle):
    def __init__(self, brand, model, year, max_speed, color, passenger_capacity):
        super().__init__(brand, model, year, max_speed, color)
        self.passenger_capacity = passenger_capacity
        self.wheels = 4
        self.doors = 2
        self.seats = 30
        self.fuel_type = "Дизель"

if __name__ == "__main__":
    car = Car("Porshe", "gtr","2020", "350", "black", "4")
    car.display_info()
    velik = Bicycle("vel", "sport", "2012", "100", "blue", "gravel")
    velik.display_info()
    motik = Motorcycle("bmw", "YZF-R1", "2008",  "250", "blue", "2")
    motik.display_info()
    truck = Truck("tesla", "cuber_truck", "2020", "200", "gray", "2500")
    truck.display_info()
    bus = Bus("USA", "schoolbus", "2005", "120", "yellow", "30")
    bus.display_info()