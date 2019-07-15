class Country:
    countries = ["India", "USA", "Russia"]

    def __init__(self):
        pass

    @classmethod
    def get_names(cls):
        return cls.countries


class City:
    cities = ["Bangalore", "New York", "Moscow"]

    def __init__(self):
        pass

    @classmethod
    def get_names(cls):
        return cls.cities
