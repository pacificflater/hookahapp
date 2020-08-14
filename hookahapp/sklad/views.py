from hookahapp.sklad.models import Manufacturer, Flavour, Mix, Membership, FlavourType
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from hookahapp.sklad.serializers import ManufacturerListSerializer, FlavourSerializer, MixSerializer, MembershipSerializer, MembershipCreateSerializer, FlavourCreateSerializer, FlavourTypeSerializer
from rest_framework import permissions, viewsets, generics

class Manufacturers(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('name')
    serializer_class = ManufacturerListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['name', 'type']


class FlavoursView(viewsets.ModelViewSet):
    queryset = Flavour.objects.all().order_by('manufacturer__name', 'flavour_name')
    permission_classes = [permissions.IsAuthenticated]
    filter_fields = ['flavour_name', 'manufacturer__name', 'manufacturer__type',  'flavour_type__type', 'in_stock']

    def get_serializer_class(self):
        if self.action == "create":
            return FlavourCreateSerializer
        elif self.action == "update":
            return FlavourCreateSerializer
        return FlavourSerializer

class FlavourTypeView(viewsets.ModelViewSet):
    serializer_class = FlavourTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = FlavourType.objects.all().order_by('type')


class MixesView(viewsets.ModelViewSet):
    serializer_class = MixSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Mix.objects.all().order_by('-rating','mix_name')
    filter_fields = ['mix_name']


class MembershipView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Membership.objects.all().order_by('flavour__flavour_name')
    def get_serializer_class(self):
        if self.action == "create":
            return MembershipCreateSerializer
        elif self.action == "update":
            return MembershipCreateSerializer
        return MembershipSerializer






