# pip install phonenumbers
import phonenumbers as phn
from phonenumbers import geocoder   # ----------->> To find the location of origin for that number
from phonenumbers import carrier    # ----------->> For the sim card used for that number
from phonenumbers import timezone   # ----------->> To get where the timezone of number exist

nmb = input("Enter phone number : ")
nmb = phn.parse(nmb)
country = geocoder.description_for_number(nmb, "en")
print("Origin ountry of number : ", country)

sim_card_prvd = carrier.name_for_number(nmb, "en")
print("Sim card provider : ", sim_card_prvd)

tmz = timezone.time_zones_for_number(nmb)
print("Time-Zone of the existing number : ", tmz)
tm = timezone.time_zones_for_geographical_number(nmb)
print(tm)