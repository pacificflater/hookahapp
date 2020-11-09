from hookahapp.sklad.models import Manufacturer, Flavour, Mix, Membership, FlavourType, ManufacturerType, BowlType, Bowl
from hookahapp.sklad.serializers import ManufacturerListSerializer, FlavourSerializer, MixSerializer, MembershipSerializer, MembershipCreateSerializer, FlavourCreateSerializer, FlavourTypeSerializer, ManufacturerTypeSerializer, ManufacturerCreateSerializer, BowlSerializer, BowlTypeSerializer, BowlCreateSerializer, MixCreateSerializer
from rest_framework import permissions, viewsets

class BowlView(viewsets.ModelViewSet):
    serializer_class = BowlSerializer
    queryset = Bowl.objects.all().order_by('name')
    permission_classes = [permissions.AllowAny]
    def get_serializer_class(self):
        if self.action == "create":
            return BowlCreateSerializer
        elif self.action == "update":
            return BowlCreateSerializer
        return BowlSerializer

class BowlTypeView(viewsets.ModelViewSet):
    serializer_class = BowlTypeSerializer
    queryset = BowlType.objects.all()
    permission_classes = [permissions.AllowAny]

class Manufacturers(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('name')
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['name', 'type']
    def get_serializer_class(self):
        if self.action == "create":
            return ManufacturerCreateSerializer
        elif self.action == "update":
            return ManufacturerCreateSerializer
        return ManufacturerListSerializer


class FlavoursView(viewsets.ModelViewSet):
    queryset = Flavour.objects.all().order_by('manufacturer__name', 'flavour_name')
    permission_classes = [permissions.AllowAny]
    filter_fields = ['flavour_name', 'manufacturer__name', 'manufacturer__type',  'flavour_type__type', 'in_stock']

    def get_serializer_class(self):
        if self.action == "create":
            return FlavourCreateSerializer
        elif self.action == "update":
            return FlavourCreateSerializer
        return FlavourSerializer

class FlavourTypeView(viewsets.ModelViewSet):
    serializer_class = FlavourTypeSerializer
    permission_classes = [permissions.AllowAny]
    queryset = FlavourType.objects.all().order_by('type')

class ManufacturerTypeView(viewsets.ModelViewSet):
    serializer_class = ManufacturerTypeSerializer
    permission_classes = [permissions.AllowAny]
    queryset = ManufacturerType.objects.all()


class MixesInStockView(viewsets.ModelViewSet):
    serializer_class = MixSerializer
    permission_classes = [permissions.AllowAny]
    flavours_out_of_stock = Flavour.objects.filter(in_stock=False)
    queryset = Mix.objects.exclude(compound__in=flavours_out_of_stock).order_by('-rating','mix_name')


class MixesView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Mix.objects.all().order_by('-rating','mix_name')
    filter_fields = ['mix_name', 'compound']
    def get_serializer_class(self):
        if self.action == "create":
            return MixCreateSerializer
        elif self.action == "update":
            return MixCreateSerializer
        return MixSerializer

class MembershipView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Membership.objects.all().order_by('flavour__flavour_name')
    def get_serializer_class(self):
        if self.action == "create":
            return MembershipCreateSerializer
        elif self.action == "update":
            return MembershipCreateSerializer
        return MembershipSerializer

# class AvailableMixesView(viewsets.ModelViewSet):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = MixSerializer
#     # queryset = Mix.objects.all().order_by('-rating','mix_name')
#     def get_queryset(self):
#         available_mixes = Mix.objects.filter(
#             compound__flavour__in_stock=True
#         ).prefetch_related(Prefetch(
#             'mix__compound',
#             queryset=Flavour.objects.filter(
#                 in_stock=True
#             ),
#         ))
#         return available_mixes






