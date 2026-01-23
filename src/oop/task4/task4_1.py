# 4.1
class Engine():
    def __init__(self, type, power, capacity):
        self.type = type
        self.power = power
        self.capacity = capacity
        
    def power_on(self):
        print('Включить двигатель')
        
    def power_of(self):
        print('Выключить двигатель')

class Car():
    def __init__(self, name, door_count, color, speed, fuel, engine: Engine):
        self.name = name
        self.door_cont = door_count
        self.color = color
        self.speed = speed
        self.fuel = fuel
        self.engine = engine

    def drive(self, new_speed):
        self.engine.power_on
        self.speed = new_speed

    def refuel(self, added_fuel_in_litres):
        self.fuel =+ added_fuel_in_litres

class SportCar(Car):
    def __init__(self, speedometer_projection, name, door_count, color, speed, fuel, engine: Engine):
        super().__init__(name, door_count, color, speed, fuel)
        self.speedometer_projection = speedometer_projection

    # Перепределение + композиция engine
    def drive(self, new_speed):
        self.engine.power_on
        self.speed = new_speed * 2

    # Перепределение
    def refuel(self, added_fuel_in_litres):
        self.fuel =+ added_fuel_in_litres * 2
