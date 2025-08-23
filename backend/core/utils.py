import geohash2
from .models import HouseAddress

def generate_address(lat, lon, country, state):
    # Step 1: geohash banao
    base_code = geohash2.encode(lat, lon, precision=9)

    # Step 2: check if already exists
    existing = HouseAddress.objects.filter(base_code=base_code).first()
    if existing:
        return existing.display_code

    # Step 3: us state ke last number find karo
    last_entry = HouseAddress.objects.filter(country=country, state=state).order_by("-short_number").first()
    next_number = 100001 if not last_entry else last_entry.short_number + 1

    # Step 4: display code banao
    display_code = f"{country}-{state}-{next_number}"

    # Step 5: save in DB
    obj = HouseAddress.objects.create(
        latitude=lat,
        longitude=lon,
        base_code=base_code,
        country=country,
        state=state,
        short_number=next_number,
        display_code=display_code
    )
    return obj.display_code
