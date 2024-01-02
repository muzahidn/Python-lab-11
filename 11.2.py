class Car:
    current_speed = 0
    travelled_distance = 0

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed

    def accelerate(self, change_of_speed):
        if change_of_speed < 0:
            if self.current_speed + change_of_speed < 0:
                self.current_speed = 0
            else:
                self.current_speed = self.current_speed - change_of_speed
        elif change_of_speed > 0:
            if self.current_speed + change_of_speed > self.maximum_speed:
                self.current_speed = self.maximum_speed
            else:
                self.current_speed = self.current_speed + change_of_speed

    def drive(self, number_of_hours_drove):
        self.travelled_distance += (self.current_speed * number_of_hours_drove)


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume


def main():
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.accelerate(100)
    gasoline_car.accelerate(80)
    electric_car.drive(3)
    gasoline_car.drive(3)

    print(f"Distance travelled by electric car: {electric_car.travelled_distance} km")
    print(f"Distance travelled by gasoline car: {gasoline_car.travelled_distance} km")


main()