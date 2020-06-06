from hookahapp.sklad.models import Manufacturer, Flavour, Membership, Mix
from rest_framework import serializers


class FlavourListSerializer(serializers.ModelSerializer):

    manufacturer_name = serializers.CharField(source='manufacturer.name')

    class Meta:
        model = Flavour
        fields = '__all__'

class ManufacturerListSerializer(serializers.ModelSerializer):

    flavours = FlavourListSerializer(many=True, read_only=True)

    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'flavours']

class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = '__all__'


class MixSerializer(serializers.ModelSerializer):

    # membership = MembershipSerializer(many=True)

    class Meta:
        model = Mix
        fields = ['mix_name', 'rating', 'strength', 'compound']


