class Car:
    def move(self):
        print("Машина едет")

    def stop(self):
        print("Машина стоит")

my_car = Car()
my_car1 = Car()

my_car.move()
my_car.stop()

my_car1.move()
my_car1.stop()

# print(my_car)
# print(type(my_car))
# print(isinstance(my_car, Car))
# print(isinstance(my_car, object))
# print(my_car == my_car1)
# print(id(my_car), id(my_car1))

print(dir(my_car))
print(my_car.dict)
class Note:
    def init(self, text):
        self.text = text
        self.count = 0

    def upcount(self):
        self.count += 1

note1 = Note("Task1")
note2 = Note("Task2")
print(note1.dict)
print(dir(note1))
print(note1.text)

note1.upcount()
print(note1.count)
note1.upcount()
print(note1.count)

class NoteTwo:
        def __init__(self, name):
            self.name = name
