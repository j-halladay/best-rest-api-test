# from django.contrib.auth.models import User, Group
from rest_api.models import ShoeType, ShoeColor, Shoe, Manufacturer
from rest_api.serializers import ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer, ManufacturerSerializer
from rest_framework import viewsets
# from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
