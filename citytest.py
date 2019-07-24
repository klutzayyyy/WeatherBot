from geotext import GeoText

places = GeoText(message.text.title())
print(places.cities[0])
