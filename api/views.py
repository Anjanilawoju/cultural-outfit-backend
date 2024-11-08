# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dresses, AddtoCart, Order
from .Serializers import DressSerializer, AddtoCartSerializer
from rest_framework import viewsets 
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view

class DressListView(APIView):
    def get(self, request):
        dresses = Dresses.objects.all()  # Fetch all dress objects
        serializer = DressSerializer(dresses, many=True)  # Serialize the queryset
        return Response(serializer.data)  # Return serialized data as a response
    
@api_view(['GET'])
def get_dresses(request, id=None):
    if id is None:
        return Response({'error': 'ID parameter is required'}, status=400)
    
    # Fetch the product by ID
    try:
        product = Dresses.objects.get(id=id)
        serializer = DressSerializer(product)
        return Response(serializer.data)
    except Dresses.DoesNotExist:
        raise NotFound(detail='Dresses not found')
    


class HotDealsView(APIView):
    def get(self, request):
        # Filter Dresses objects where category is "hot deals"
        hot_deals = Dresses.objects.filter(category="hot deals")

        # Serialize the filtered queryset
        hot_deals_serializer = DressSerializer(hot_deals, many=True)

        # Return the serialized data
        return Response(hot_deals_serializer.data, status=status.HTTP_200_OK)

class OurPicksView(APIView):
    def get(self, request):
        # Filter Dresses objects where category is "our picks"
        our_picks = Dresses.objects.filter(category="our picks")

        # Serialize the filtered queryset
        our_picks_serializer = DressSerializer(our_picks, many=True)

        # Return the serialized data
        return Response(our_picks_serializer.data, status=status.HTTP_200_OK)
    
    
class NewariDress(APIView):
    def get(self, request):
        # Filter Dresses objects where category is "our picks"
        newari = Dresses.objects.filter(category="newari")

        # Serialize the filtered queryset
        newari_serializer = DressSerializer(newari, many=True)

        # Return the serialized data
        return Response(newari_serializer.data, status=status.HTTP_200_OK)
    
class TamangDress(APIView):
    def get(self, request):
        # Filter Dresses objects where category is "our picks"
        tamang = Dresses.objects.filter(category="tamang")

        # Serialize the filtered queryset
        tamang_serializer = DressSerializer(tamang, many=True)

        # Return the serialized data
        return Response(tamang_serializer.data, status=status.HTTP_200_OK)
    
class GurungDress(APIView):
    def get(self, request):
        # Filter Dresses objects where category is "our picks"
        gurung = Dresses.objects.filter(category="gurung")

        # Serialize the filtered queryset
        gurung_serializer = DressSerializer(gurung, many=True)

        # Return the serialized data
        return Response(gurung_serializer.data, status=status.HTTP_200_OK)
    
class SherpaDress(APIView):
    def get(self, request):
        # Filter Dresses objects where category is "our picks"
        sherpa = Dresses.objects.filter(category="sherpa")

        # Serialize the filtered queryset
        sherpa_serializer = DressSerializer(sherpa, many=True)

        # Return the serialized data
        return Response(sherpa_serializer.data, status=status.HTTP_200_OK)
    
class MagarDress(APIView):
    def get(self, request):
        # Filter Dresses objects where category is "our picks"
        magar = Dresses.objects.filter(category="magar")

        # Serialize the filtered queryset
        magar_serializer = DressSerializer(magar, many=True)

        # Return the serialized data
        return Response(magar_serializer.data, status=status.HTTP_200_OK)
    
class TharuDress(APIView):
    def get(self, request):
        # Filter Dresses objects where category is "our picks"
        tharu = Dresses.objects.filter(category="tharu")

        # Serialize the filtered queryset
        tharu_serializer = DressSerializer(tharu, many=True)

        # Return the serialized data
        return Response(tharu_serializer.data, status=status.HTTP_200_OK)

class NewArrival(APIView):
    def get(self, request):
        # Filter Dresses objects where category is "new arrival"
        newarrival = Dresses.objects.filter(category="new arrival")

        # Serialize the filtered queryset
        newarrival_serializer = DressSerializer(newarrival, many=True)

        # Return the serialized data
        return Response(newarrival_serializer.data, status=status.HTTP_200_OK)
    
class AddtoCartViewSet(viewsets.ModelViewSet):
    queryset = AddtoCart.objects.all()
    serializer_class = AddtoCartSerializer