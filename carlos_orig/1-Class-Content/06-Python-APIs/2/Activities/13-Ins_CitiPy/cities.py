# Dependencies
from citipy import citipy

# Some random coordinates
coordinates = [(200, 200), (23, 200), (42, 100)]

cities = []
for coordinate_pair in coordinates:
    lat, lon = coordinate_pair
    cities.append(citipy.nearest_city(lat, lon))

for city in cities:
    country_code = city.country_code
    name = city.city_name
    print("The country code of " + name + " is '" + country_code + "'.")
