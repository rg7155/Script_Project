import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBX0HsOdoPKvvxqvzbSXhDGdi4dsKfYU7Q')

# # Geocoding an address
# geocode_result = gmaps.geocode('필운동 신동아블루아광화문의 꿈', language='ko')
#
# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
#
# #lat, lng
# print(geocode_result[0]['geometry']['location'])

def getGeocode(str):
    geocode_result = gmaps.geocode(str, language='ko')
    return geocode_result[0]['geometry']['location']

