# Создай объект Машина, которому можно задать свойства цвет и
# марку при создании.
# И методы ехать и остановиться.
# А также можно будет заменить владельца авто.

class Car:
    def __init__(self, brand, color):  # (self, car):
        self.brand = brand  # self.car = car
        self.color = color

    def drive(self):
        return 'I`m drive!'

    def stop(self):
        return 'I`m stopped!!!'

    def change_owner(self):
        self.driver
        return 'What?'


car = Car('Toyota', 'black')
# car.drive('hi')

print(car.brand, car.color)
print(car.drive())  # I'm runned
print(car.stop())  # I'm stoped
print(car.change_owner('Pit'))
# print(car.change_owner('New owner'))

