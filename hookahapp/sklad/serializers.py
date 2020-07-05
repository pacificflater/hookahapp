from rest_framework import serializers

from hookahapp.sklad.models import Flavour, Manufacturer, Membership, Mix



class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'





class FlavourCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavour
        fields = ['id', 'flavour_name', 'manufacturer', 'in_stock', 'add_time']

class FlavourSerializer(FlavourCreateSerializer):
    manufacturer = ManufacturerSerializer()

class ManufacturerListSerializer(serializers.ModelSerializer):
    flavours = FlavourSerializer(many=True, read_only=True)

    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'flavours']


class MembershipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['id', 'percentage', 'mix', 'flavour']


class MembershipSerializer(MembershipCreateSerializer):
    flavour = FlavourSerializer()


class MixSerializer(serializers.ModelSerializer):

    compound = MembershipSerializer(many=True, read_only=True,  source='membership_set')

    class Meta:
        model = Mix
        fields = ['id', 'mix_name', 'rating', 'strength', 'compound']
