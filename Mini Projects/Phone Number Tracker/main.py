import phonenumbers

from phonenumbers import geocoder
number=input("Enter Phone Number Along with +Country Code: ")
coutry_name=phonenumbers.parse(number,"CH")
print("Country:-> ",geocoder.description_for_number(coutry_name,"en"))

from phonenumbers import carrier
service_provider=phonenumbers.parse(number,"RO")
print("Service Provider:-> ",carrier.name_for_number(service_provider,"en"))

from phonenumbers import timezone
time_zone= phonenumbers.parse(number, "GB")
print("Time Zone:-> ",timezone.time_zones_for_number(time_zone))
