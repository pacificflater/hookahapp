from hookahapp.sklad.models import Manufacturer, Flavour, Membership, Mix
from rest_framework import serializers


class FlavourListSerializer(serializers.ModelSerializer):

    manufacturer_name = serializers.CharField(source='manufacturer.name', read_only=True)

    class Meta:
        model = Flavour
        fields = '__all__'

class ManufacturerListSerializer(serializers.ModelSerializer):

    flavours = FlavourListSerializer(many=True, read_only=True)

    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'flavours']

class MembershipSerializer(serializers.ModelSerializer):

    flavour_name = serializers.CharField(source='flavour.flavour_name')
    flavour_id = serializers.CharField(source='flavour.id')
    flavour = FlavourListSerializer(many=True)

    class Meta:
        model = Membership
        fields = ['persontage', 'mix', 'flavour']

class MixSerializer(serializers.ModelSerializer):

    # compound = MembershipSerializer(many=True)

    class Meta:
        model = Mix
        fields = ['id', 'mix_name', 'rating', 'strength', 'compound']


