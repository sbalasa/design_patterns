class Car:
    car_name = ""

    @classmethod
    def display(cls):
        print(cls.car_name)


class Ford(Car):
    car_name = "Ford Mustang GT"


class Toyota(Car):
    car_name = "Toyota Yaris"


class Audi(Car):
    car_name = "Audi A8"


def main() -> object:
    for car in ["ford", "toyota", "audi"]:
        globals()[car.capitalize()].display()


if __name__ == "__main__":
    main()
