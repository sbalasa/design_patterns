from car_type import Sedan, Hatchback, SUV


class Builder:
    __builder = None

    @classmethod
    def set_builder(cls, build):
        cls.__builder = build

    @classmethod
    def build(cls):
        car = {
            "horsepower": cls.__builder.engine * 100,
            "wheels": f"4 x {cls.__builder.wheel_size}",
            "shape": cls.__builder.shape,
            "seats": cls.__builder.seats
        }
        for component, component_value in car.items():
            print(component, "->", component_value)


def main():
    print("-----------------------")
    # Build a Sedan
    car_builder = Builder()
    car_builder.set_builder(Sedan)
    car_builder.build()

    print("-----------------------")
    # Build a Hatchback
    car_builder.set_builder(Hatchback)
    car_builder.build()

    print("-----------------------")
    # Build a SUV
    car_builder.set_builder(SUV)
    car_builder.build()


if __name__ == "__main__":
    main()
