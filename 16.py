# class Car:
#
#     def __init__(self, marka, year, max_speed):
#         self.__marka = marka
#         self.__year = Year
#         self.__max_speed = Max_speed
#
#     def get_marka(self):
#         self.__marka = bmw
#     def
#
#     def get_year(self):
#         self.__year = 2022
#
#     def set_max_speed(self):
#         self.__max_speed = 321
#
#
#
# bmw = car
#
# class Person:
#     def __init__(self, name, surname, age):
#         self.__name = name
#         self.__surname = surname
#         self.__age = age
#
#     def get_name(self):
#         self.__name = "Bakyt"
#
#     def get_surname(self):
#         self.__surname = "Asanov"
#
#     def get_age(self):
#         self.__age = 17
#
#     def sing(self):
#         print(f"{self.__name} is to sing")
#
#     def write(self):
#         print(f"{self.__name} is to writing")
#
#     def get_info(self):
#         print(f"name: {self.get_name()}/n"
#               f"surname: {self.get_surname()}/n"
#               f"age: {self.get_age()}")
#
# Bakyt = Person("Asan", )
#
# class Profession:
#     def __init__(self, offesiant, manager, prodovets, teacher):
#         self.__offesiant = off
#         self.__manager = manager
#         self.__prodovets = prodov
#         self.__teacher = teacher
#     def get_off(self):
#         self.__offesiant = "1st smena"
#
#     def get_manager(self):
#         self.__manager = "piece of papers"
#
#     def get_prodov(self):
#         self.__prodovets = "tovary"
#
#     def get_teacher(self):
#         self.__teacher = "children"


class Profession:
    def __init__(self, name, field, skills):
        self.name = name
        self.field = field
        self.skills = skills

    def get_info(self):
        print(f"Профессия: {self.name}")
        print(f"Сфера: {self.field}")
        print("Навыки:", ", ".join(self.skills)


programmer = Profession("Программист", "IT", ["Python"])
print(programmer)
teacher = Profession("Учитель","Языка", ["Английского"])
print(teacher)
engineer = Profession("Инженер", "Строительство", ["Анализ", "Математика", "Управление проектами"])
print(engineer)
povar = Profession("Повар", "Кондитер", ["Торты, Конфеты", "Десерты"])
print(povar)