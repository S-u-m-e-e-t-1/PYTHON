import phonenumbers
import  opencage
import folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import   OpenCageGeocode
# Example phone number (replace with actual number)
phone_number = phonenumbers.parse("+918506846568")
key="ee4a5ca8353a40f2816d386788a27242"
# Get location
location = geocoder.description_for_number(phone_number, "en")
print("Location:", location)

# Get carrier
service_provider = carrier.name_for_number(phone_number, "en")
print("Carrier:", service_provider)

geocoder=OpenCageGeocode(key)
query=str(location)
result=geocoder.geocode(query)
# print(result)

lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=10)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("location.html")
