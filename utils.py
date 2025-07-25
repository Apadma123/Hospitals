from geopy.geocoders import Nominatim
from math import radians, sin, cos, sqrt, atan2

geolocator = Nominatim(user_agent="navigator")

async def get_coordinates(zip_code: str):
    location = geolocator.geocode(zip_code)
    if location:
        return location.latitude, location.longitude
    return None, None

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))
