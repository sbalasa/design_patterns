from model import City, Country


def display():
    print("List of countries:")
    [print("    -", country,) for country in Country.get_names()]
    print("List of cities:")
    [print("    -", city,) for city in City.get_names()]
