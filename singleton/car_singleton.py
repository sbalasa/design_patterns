def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class Car:
    cars = []

    @classmethod
    def add_car(cls, name):
        cls.cars.append(name)

    @classmethod
    def display(cls):
        [print(car,) for car in cls.cars]


def main():
    car_object = Car()
    car_object1 = Car()
    car_object1.add_car("Ford Mustang GT")
    car_object2 = Car()
    car_object2.add_car("Toyota Yaris")
    car_object3 = Car()
    car_object3.add_car("Audi A8")
    car_object.display()


if __name__ == "__main__":
    main()
