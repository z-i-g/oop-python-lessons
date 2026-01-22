class Car():
    def __init__(self, name, door_count, color, speed, fuel):
        self.name = name
        self.door_cont = door_count
        self.color = color
        self.speed = speed
        self.fuel = fuel

    def drive(self, new_speed):
        self.speed = new_speed

    def refuel(self, added_fuel_in_litres):
        self.fuel =+ added_fuel_in_litres

class SportCar(Car):
    def __init__(self, name, door_count, color, speed, speedometer_projection):
        super().__init__(name, door_count, color, speed)
        self.speedometer_projection = speedometer_projection

    # Перепределение
    def drive(self, new_speed):
        self.speed = new_speed * 2

    # Перепределение
    def refuel(self, added_fuel_in_litres):
        self.fuel =+ added_fuel_in_litres * 2

class Truck(Car):
    def __init__(self, name, door_count, color, speed, load_capacity):
        super().__init__(name, door_count, color, speed)
        self.load_capacity = load_capacity

    # Перепределение
    def drive(self, new_speed):
        self.speed = new_speed / 2

    # Перепределение
    def refuel(self, added_fuel_in_litres):
        self.fuel =+ added_fuel_in_litres * 4



class Engine():
    def __init__(self, type, power, capacity):
        self.type = type
        self.power = power
        self.capacity = capacity
        
    def power_on(self):
        print('Включить двигатель')
        
    def power_of(self):
        print('Выключить двигатель')

class PetrolEngine(Engine):
    def __init__(self, type, power, capacity, exhaust_system):
        super.__init__(type, power, capacity)
        self.type = type
        self.power = power
        self.capacity = capacity
        self.exhaust_system = exhaust_system
        
    def power_on(self):
        print('Включить двигатель')
        print('Активировать выхлопную систему двигатель')
        
    def power_of(self):
        print('Выключить двигатель')
        print('Деактивировать выхлопную систему двигатель')

class ElectricMotor (Engine):
    def __init__(self, type, power, capacity, accumulator):
        super.__init__(type, power, capacity)
        self.type = type
        self.power = power
        self.capacity = capacity
        self.accumulator = accumulator
        
    def power_on(self):
        print('Проверить уровень заряда батареи')
        print('Включить двигатель')
        
    def power_of(self):
        print('Выключить двигатель')
        print('Перевейти в энергосберегающий режим батареи')