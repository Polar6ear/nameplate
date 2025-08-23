from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import generate_address

@api_view(["POST"])
def create_address(request):
    lat = float(request.data.get("latitude"))
    lon = float(request.data.get("longitude"))
    country = request.data.get("country")   # "IN"
    state = request.data.get("state")       # "DL"

    code = generate_address(lat, lon, country, state)
    return Response({"code": code})