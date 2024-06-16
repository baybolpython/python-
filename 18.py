class House:
    def __init__(self, door, window, rooms):
        self.__door = door
        self.__window = window
        self.__rooms = rooms
    def get_door(self):
        return self.__door
    def set_door(self):
        self.__door = door

    def get_rooms(self):
        return self.__rooms
    def set_rooms(self):
        self.__rooms = rooms

    def get_window(self):
        return self.__window
    def set_window(self):
        self.__window = window

    def get_info(self):
        print(f"rooms {self.get_rooms()}/n"
              f"window {self.get_window()}/n"
              f"door {self.get_door()}/n")

class Garage(House):
    def __init__(self, have_car, instrumenty):
        self.__have_car = have_car
        self.__instrumenty = instrumenty


    def get_havaaaaaaaaaaaaasa e_car(self):
        return self.__have_car
    def set_have_car(self):
        self.__