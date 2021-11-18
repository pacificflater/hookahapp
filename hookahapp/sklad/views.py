from hookahapp.sklad.models import Manufacturer, Flavour, Mix, Membership, FlavourType, ManufacturerType, BowlType, Bowl
from hookahapp.sklad.serializers import ManufacturerListSerializer, FlavourSerializer, MixSerializer, MembershipSerializer, MembershipCreateSerializer, FlavourCreateSerializer, FlavourTypeSerializer, ManufacturerTypeSerializer, ManufacturerCreateSerializer, BowlSerializer, BowlTypeSerializer, BowlCreateSerializer, MixCreateSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.shortcuts import render

class BowlView(viewsets.ModelViewSet):
    serializer_class = BowlSerializer
    queryset = Bowl.objects.all().order_by('name')
    permission_classes = [AllowAny]
    def get_serializer_class(self):
        if self.action == "create":
            return BowlCreateSerializer
        elif self.action == "update":
            return BowlCreateSerializer
        return BowlSerializer

class BowlTypeView(viewsets.ModelViewSet):
    serializer_class = BowlTypeSerializer
    queryset = BowlType.objects.all()
    permission_classes = [AllowAny]

class Manufacturers(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('name')
    permission_classes = [AllowAny]
    filterset_fields = ['name', 'type']
    def get_serializer_class(self):
        if self.action == "create":
            return ManufacturerCreateSerializer
        elif self.action == "update":
            return ManufacturerCreateSerializer
        return ManufacturerListSerializer


class FlavoursView(viewsets.ModelViewSet):
    queryset = Flavour.objects.all().order_by('manufacturer__name', 'flavour_name')
    permission_classes = [AllowAny]
    filter_fields = ['flavour_name', 'manufacturer__name', 'manufacturer__type',  'flavour_type__type', 'in_stock']

    def get_serializer_class(self):
        if self.action == "create":
            return FlavourCreateSerializer
        elif self.action == "update":
            return FlavourCreateSerializer
        return FlavourSerializer

class FlavourTypeView(viewsets.ModelViewSet):
    serializer_class = FlavourTypeSerializer
    permission_classes = [AllowAny]
    queryset = FlavourType.objects.all().order_by('type')

class ManufacturerTypeView(viewsets.ModelViewSet):
    serializer_class = ManufacturerTypeSerializer
    permission_classes = [AllowAny]
    queryset = ManufacturerType.objects.all()


class MixesInStockView(viewsets.ModelViewSet):
    serializer_class = MixSerializer
    permission_classes = [AllowAny]
    flavours_out_of_stock = Flavour.objects.filter(in_stock=False)
    queryset = Mix.objects.exclude(compound__in=flavours_out_of_stock).order_by('-rating','mix_name')


class MixesView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Mix.objects.all().order_by('-rating','mix_name')
    filter_fields = ['mix_name', 'compound']
    def get_serializer_class(self):
        if self.action == "create":
            return MixCreateSerializer
        elif self.action == "update":
            return MixCreateSerializer
        return MixSerializer

class MembershipView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Membership.objects.all().order_by('flavour__flavour_name')
    def get_serializer_class(self):
        if self.action == "create":
            return MembershipCreateSerializer
        elif self.action == "update":
            return MembershipCreateSerializer
        return MembershipSerializer

def index(request, path=''):
    """
    Renders the Angular2 SPA
    """

    return render(request, 'index.html')


