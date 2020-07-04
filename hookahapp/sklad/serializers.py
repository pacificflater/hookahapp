from rest_framework import serializers

from hookahapp.sklad.models import Flavour, Manufacturer, Membership, Mix


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class FlavourSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Flavour
        fields = ['id', 'flavour_name', 'manufacturer', 'in_stock', 'add_time']


class ManufacturerListSerializer(serializers.ModelSerializer):
    flavours = FlavourSerializer(many=True, read_only=True)

    class Meta:
        model = Manufacturer
        # fields = '__all__'
        fields = ['id', 'name', 'flavours']


class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = ['percentage', 'mix', 'flavour']

    # def create(self, validated_data):
    #     flavours_data = validated_data.pop('flavour')
    #     membership = Membership.objects.create(**validated_data)
    #     for flavour_data in flavours_data:
    #         Flavour.objects.create(membership=membership, **flavour_data)
    #     return membership


class MixSerializer(serializers.ModelSerializer):

    compound = MembershipSerializer(many=True, read_only=True,  source='membership_set')

    class Meta:
        model = Mix
        fields = ['id', 'mix_name', 'rating', 'strength', 'compound']

    # def create(self, validated_data):
    #     #     compound_data = validated_data.pop('compound')
    #     #     mix = Mix.objects.create(**validated_data)
    #     #     for compound_data in compound_data:
    #     #         Mix.objects.create(mix=mix, **compound_data)
    #     #     return mix
