```python
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from opencage.geocoder import OpenCageGeocode

# Ganti dengan API key OpenCage kamu
API_KEY = 'API_KEY_OPENCAGE'

def track_phone_number(phone_number):
    # Parse nomor HP
    parsed_number = phonenumbers.parse(phone_number, None)

    # Dapetin operator
    operator = carrier.name_for_number(parsed_number, 'id')

    # Dapetin lokasi berdasarkan nomor
    location = geocoder.description_for_number(parsed_number, 'id')

    # Dapetin timezone
    time_zone = timezone.time_zones_for_number(parsed_number)

    # Dapetin koordinat pake OpenCage
    geocoder = OpenCageGeocode(API_KEY)
    results = geocoder.geocode(location)

    if results and len(results):
        latitude = results[0]['geometry']['lat']
        longitude = results[0]['geometry']['lng']
    else:
        latitude, longitude = None, None

    # Print hasil
    print(f"Nomor: {phone_number}")
    print(f"Operator: {operator}")
    print(f"Lokasi: {location}")
    print(f"Timezone: {time_zone}")
    print(f"Koordinat: Latitude {latitude}, Longitude {longitude}")
