class BMW:
    def start(self):
        print("BMW engine starts with a smooth ignition.")

    def speed(self):
        print("BMW top speed is 250 km/h.")


class Ferrari:
    def start(self):
        print("Ferrari engine roars to life!")

    def speed(self):
        print("Ferrari top speed is 340 km/h.")


def car_details(car):
    car.start()
    car.speed()


bmw_car = BMW()
ferrari_car = Ferrari()

car_details(bmw_car)
car_details(ferrari_car)
