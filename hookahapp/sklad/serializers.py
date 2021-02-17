from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from hookahapp.sklad.models import Flavour, Manufacturer, Membership, Mix, FlavourType, ManufacturerType, BowlType, Bowl

class BowlTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BowlType
        fields = ['id', 'type']
        validators = [
            UniqueTogetherValidator(
                queryset=BowlType.objects.all(),
                fields=['type'],
                message='Such bowl type already exists'
            )
        ]

class BowlSerializer(serializers.ModelSerializer):
    type = BowlTypeSerializer(read_only=True)
    class Meta:
        model = Bowl
        fields = '__all__'

class BowlCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bowl
        fields = ['name', 'type']
        validators = [
            UniqueTogetherValidator(
                queryset=Bowl.objects.all(),
                fields=['name'],
                message='Such bowl name already exists'
            )
        ]

class ManufacturerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManufacturerType
        fields = ['id', 'type']
        validators = [
            UniqueTogetherValidator(
                queryset=ManufacturerType.objects.all(),
                fields=['type'],
                message='Such manufacturer type already exists'
            )
        ]

class ManufacturerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'type']

    validators = [
        UniqueTogetherValidator(
            queryset=Manufacturer.objects.all(),
            fields=['name'],
            message='Such manufacturer name already exists'
        )
    ]

class ManufacturerSerializer(serializers.ModelSerializer):
    type = ManufacturerTypeSerializer(read_only=True)
    class Meta:
        model = Manufacturer
        fields = '__all__'

class FlavourTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlavourType
        fields = ['id', 'type']
        validators = [
            UniqueTogetherValidator(
                queryset=FlavourType.objects.all(),
                fields=['type'],
                message='Such flavour type already exists'
            )
        ]

class FlavourCreateSerializer(serializers.ModelSerializer):
    class Meta:

        model = Flavour
        fields = ['id', 'flavour_name', 'manufacturer', 'flavour_type', 'in_stock', 'description', 'add_time']

        validators = [
            UniqueTogetherValidator(
                queryset = Flavour.objects.all(),
                fields = ['flavour_name', 'manufacturer'],
                message='Such flavour already exists'
            )
        ]


class FlavourSerializer(FlavourCreateSerializer):
    manufacturer = ManufacturerSerializer()
    flavour_type = FlavourTypeSerializer(many=True, read_only=True)

class ManufacturerListSerializer(serializers.ModelSerializer):
    flavour = FlavourSerializer(many=True, read_only=True)
    type = ManufacturerTypeSerializer(read_only=True)

    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'type', 'flavour']



class MembershipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['id', 'percentage', 'mix', 'flavour']
        validators = [
            UniqueTogetherValidator(
                queryset=Membership.objects.all(),
                fields=['mix', 'flavour'],
                message='Such Membership already exists'
            )
        ]


class MembershipSerializer(MembershipCreateSerializer):
    flavour = FlavourSerializer()


class MixSerializer(serializers.ModelSerializer):

    compound = MembershipSerializer(many=True, read_only=True,  source='membership_set')
    bowl = BowlSerializer(many=False, read_only=True)

    class Meta:
        model = Mix
        fields = ['id', 'mix_name', 'rating', 'strength', 'compound', 'bowl', 'description']

class MixCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mix
        fields = ['id', 'mix_name', 'rating', 'strength', 'compound', 'bowl', 'description']
        validators = [
            UniqueTogetherValidator(
                queryset=Mix.objects.all(),
                fields=['mix_name'],
                message='Such Mix name already exists'
            )
        ]