from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import UserLocation

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def save_location(request):
    lat = request.data.get("latitude")
    lon = request.data.get("longitude")
    
    if not lat or not lon:
        return Response({"error": "Latitude and longitude required"}, status=400)

    UserLocation.objects.create(
        user=request.user,
        latitude=lat,
        longitude=lon
    )

    return Response({"message": "Location saved successfully!"})
