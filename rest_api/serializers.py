from rest_api.models import ShoeType, ShoeColor, Shoe, Manufacturer
from rest_framework import serializers


class ShoeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ['color_name']


class ShoeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ['style']


class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = ['brand_name', 'manufacturer', 'color',
                  'material', 'shoe_type', 'fasten_type']


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'website']
