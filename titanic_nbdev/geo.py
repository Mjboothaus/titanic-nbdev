# AUTOGENERATED! DO NOT EDIT! File to edit: 01_geo.ipynb (unless otherwise specified).

__all__ = ['lookup_lat_lon_from_placename']

# Cell
def lookup_lat_lon_from_placename(place):
    geolocator = Nominatim(user_agent="DataBooth")
    try:
        location = geolocator.geocode(place)
    except Exception as e:
        print(e)
    return location.latitude, location.longitude